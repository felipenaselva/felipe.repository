"""
    SALTS XBMC Addon
    Copyright (C) 2014 tknorris

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import re
import urllib
import urlparse
import string
import random
import time
import base64
import hashlib
import kodi
import log_utils
import dom_parser
from salts_lib import scraper_utils
from salts_lib.constants import FORCE_NO_MATCH
from salts_lib.constants import QUALITIES
from salts_lib.constants import VIDEO_TYPES
from salts_lib.constants import XHR
import scraper

BASE_URL = 'http://movieshd.watch'
EMBED_URL = '/ajax/embeds.php'
SEARCH_URL = '/api/v1/cautare/upd'
KEY = 'MEE2cnUzNXl5aTV5bjRUSFlwSnF5MFg4MnRFOTVidFY='

class Scraper(scraper.Scraper):
    base_url = BASE_URL
    __token = None
    __t = None

    def __init__(self, timeout=scraper.DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.base_url = kodi.get_setting('%s-base_url' % (self.get_name()))

    @classmethod
    def provides(cls):
        return frozenset([VIDEO_TYPES.MOVIE])

    @classmethod
    def get_name(cls):
        return 'MoviesHD'

    def get_sources(self, video):
        source_url = self.get_url(video)
        sources = []
        if source_url and source_url != FORCE_NO_MATCH:
            url = urlparse.urljoin(self.base_url, source_url)
            html = self._http_get(url, cache_limit=2)
            match = re.search('defaultStream.movie\s*=\s*"([^"]+)', html)
            links = [match.group(1)] if match else []
            
            if video.video_type == VIDEO_TYPES.MOVIE:
                action = 'getMovieEmb'
            else:
                action = 'getEpisodeEmb'
                
            if self.__token is None:
                self.__get_token()
                
            match = re.search('elid\s*=\s*"([^"]+)', html)
            if match and self.__token is not None:
                elid = urllib.quote(base64.encodestring(str(int(time.time()))).strip())
                data = {'action': action, 'idEl': match.group(1), 'token': self.__token, 'elid': elid}
                ajax_url = urlparse.urljoin(self.base_url, EMBED_URL)
                headers = {'Authorization': 'Bearer %s' % (self.__get_bearer()), 'Referer': url}
                headers.update(XHR)
                html = self._http_get(ajax_url, data=data, headers=headers, allow_redirect=False, cache_limit=0)
                ajax_url += '?ckattempt=1'
                html = self._http_get(ajax_url, data=data, headers=headers, cache_limit=0)
                html = html.replace('\\"', '"').replace('\\/', '/')
                links += dom_parser.parse_dom(html, 'iframe', ret='src')
                
            for stream_url in links:
                host = self._get_direct_hostname(stream_url)
                if host == 'gvideo':
                    direct = True
                    quality = scraper_utils.gv_get_quality(stream_url)
                else:
                    if 'vk.com' in url and stream_url.endswith('oid='): continue  # skip bad vk.com links
                    direct = False
                    host = urlparse.urlparse(stream_url).hostname
                    quality = scraper_utils.get_quality(video, host, QUALITIES.HD720)

                source = {'multi-part': False, 'url': stream_url, 'host': host, 'class': self, 'quality': quality, 'views': None, 'rating': None, 'direct': direct}
                sources.append(source)

        return sources

    def search(self, video_type, title, year, season=''):
        results = []
        self.__get_token()
        if self.__token is not None:
            search_url = urlparse.urljoin(self.base_url, self.__get_search_url())
            timestamp = int(time.time() * 1000)
            s = self.__get_s()
            query = {'q': title, 'limit': '100', 'timestamp': timestamp, 'verifiedCheck': self.__token, 'set': s,
                     'rt': self.__get_rt(self.__token + s), 'sl': self.__get_sl(search_url)}
            headers = XHR
            headers['Referer'] = self.base_url
            html = self._http_get(search_url, data=query, headers=headers, cache_limit=8)
            log_utils.log(html)
            if video_type in [VIDEO_TYPES.TVSHOW, VIDEO_TYPES.EPISODE]:
                media_type = 'TV SHOW'
            else:
                media_type = 'MOVIE'
    
            for item in scraper_utils.parse_json(html, search_url):
                if item['meta'].upper().startswith(media_type):
                    match_year = str(item['year']) if 'year' in item and item['year'] else ''
                    if not year or not match_year or year == match_year:
                        result = {'title': scraper_utils.cleanse_title(item['title']), 'url': scraper_utils.pathify_url(item['permalink']), 'year': match_year}
                        results.append(result)

        return results

    def __get_bearer(self):
        cj = self._set_cookies(self.base_url, {})
        for cookie in cj:
            if cookie.name == '__utmx':
                return cookie.value
    
    def __get_search_url(self):
        search_url = SEARCH_URL
        return search_url
    
    def __get_token(self, html=''):
        if self.__token is None:
            if not html:
                html = super(self.__class__, self)._http_get(self.base_url, cache_limit=8)
                
            match = re.search("var\s+tok\s*=\s*'([^']+)", html)
            if match:
                self.__token = match.group(1)
            else:
                log_utils.log('Unable to locate MoviesHD token', log_utils.LOGWARNING)
    
    def __get_s(self):
        return ''.join([random.choice(string.ascii_letters) for _ in xrange(25)])
    
    def __get_rt(self, s, shift=13):
        s2 = ''
        for c in s:
            limit = 122 if c in string.ascii_lowercase else 90
            new_code = ord(c) + shift
            if new_code > limit:
                new_code -= 26
            s2 += chr(new_code)
        return s2

    def __get_sl(self, url):
        u = url.split('/')[-1]
        return hashlib.md5(KEY + u).hexdigest()
        
        
        