# -*- coding: utf-8 -*-

'''
    Exodus Add-on
    Copyright (C) 2016 Exodus

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
'''


import re,urllib,urlparse,json,base64

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import dom_parser
from resources.lib.modules import directstream
from resources.lib.modules import source_utils
from resources.lib.modules import log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['pubfilm.to']
        self.base_link = 'http://pubfilm.to'
        self.moviesearch_link = '/%s-%s-full-hd-pubfilm-free.html'
        self.moviesearch_link_2 = '/%s-%s-pubfilm-free.html'

        self.tvsearch_link = '?c=movie&m=quickSearch&keyword=%s'
        self.tvsearch_link_2 = '/?s=%s'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            return self.__search([title] + source_utils.aliases_to_array(aliases), year)
        except:
            return


    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'tvshowtitle': tvshowtitle, 'aliases': aliases, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            tvshowtitle = data['tvshowtitle']
            aliases = source_utils.aliases_to_array(eval(data['aliases']))
            # maybe ignore the year because they use wrong dates on seasons
            url = self.__search([tvshowtitle] + aliases, data['year'], season)

            #if url == None: raise Exception()
            if not url: return

            url += '%01d' % int(episode)
            url = urlparse.urljoin(self.base_link, url)
            url = url.encode('utf-8')
            return url
        except:
            traceback.print_exc()
            return

    def __search(self, titles, year, season='0'):
        try:
            url = urlparse.urljoin(self.base_link, self.tvsearch_link) % (urllib.quote_plus(titles[0]))
            result = client.request(url)
            if season <> '0':
                id = [j['id'] for j in json.loads(result) if str.upper(str(j['title'])) == str.upper(titles[0] + ' - Season ' + season) ]
                page = '%s-season-%s-stream-%s.html' % (str.replace(titles[0],' ','-'), season, id[0])
                
            else:
                id = [j['id'] for j in json.loads(result) if str.upper(str(j['title'])) == str.upper(titles[0]) and j['year'] == year ]
                page = '%s-stream-%s.html' % (str.replace(titles[0],' ','-'), id[0])
            
            url = urlparse.urljoin(self.base_link, page)
            result = client.request(url)
            url = re.findall(u'<center><iframe\s+id="myiframe".*?src="([^"]+)', result)[0]
            result = client.request(url)
            rex = 'href=\'([^\']+episode=)' if season <> '0' else 'class="server(?:Active)?"><a\s+href="([^"]+)"'
            url = re.findall(rex, result)[0]           
            return url
        except:
            traceback.print_exc()
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url == None: return sources

            content = re.compile('(.+?)&server=.+&episode=\d*$').findall(url)
            content = 'movie' if len(content) == 0 else 'episode'

            if content <> 'movie':
                try: 
                    uri, server, episode = re.compile('(.+?)&server=(.+)&episode=(\d*)$').findall(url)[0]
                    url1 = '%s&server=1&episode=%s' % (uri,episode)
                except:
                    url1 = url
            else: url1 = url

            
            for i in range(3):
                result = client.request(url1, timeout='10')
                if not result == None: break
            try:
                data = re.findall('>({"data".*]})<', result)[0]
                data = json.loads(data)
                links_ = data['data']
                links = []
                for l in links_: links.append(l['files'])               
            except:
                links = re.findall(r"<source\s+src='([^>]+)>", result)
              

            for u in links:
                try:
                    u = str.replace(str(u),"'","")
                    l = re.findall('^http[^\s]+', u)[0]
                    valid, hoster = source_utils.is_host_valid(l, hostDict)
                    if not valid: continue
                    l = directstream.googletag(l)[0]
                    sources.append({'source': 'gvideo', 'quality': l['quality'], 'language': 'en', 'url': l['url'], 'direct': True, 'debridonly': False})
                   
                except:
                    pass            
            
            #log_utils.log('Jairox5: %s' % (str(sources)), log_utils.LOGDEBUG) 
            return sources
        except:
            return sources


    def resolve(self, url):
        return directstream.googlepass(url)
        #return url


