#!/usr/bin/python
import xbmc, sys, os
from .base import _Base, _MetaClass
from kodipopcorntime.exceptions import Error

__addon__ = sys.modules['__main__'].__addon__

class Addon(_Base):
    class __metaclass__(_MetaClass):
        def _base_url(cls):
            cls.base_url = sys.argv[0]

        def _handle(cls):
            cls.handle = int(sys.argv[1])

        def _cur_uri(cls):
            cls.cur_uri = sys.argv[2][1:]

        def _language(cls):
            cls.language = xbmc.getLanguage(xbmc.ISO_639_1)

        def _cache_path(cls):
            _path = xbmc.translatePath("special://profile/addon_data/%s/cache" % cls.id)
            if not os.path.exists(_path):
                os.makedirs(_path)
                if not os.path.exists(_path):
                    raise Error("Unable to create cache directory %s" % _path, 30322)
            cls.cache_path = _path.encode(cls.fsencoding)

        def _resources_path(cls):
            cls.resources_path = os.path.join(__addon__.getAddonInfo('path'), 'resources')

        def _debug(cls):
            if __addon__.getSetting("debug") == 'true':
                cls.debug = True
            else:
                cls.debug = False

        def _id(cls):
            cls.id = __addon__.getAddonInfo('id')

        def _name(cls):
            cls.name = __addon__.getAddonInfo('name')

        def _version(cls):
            cls.version = __addon__.getAddonInfo('version')

        def _fanart(cls):
            cls.fanart = __addon__.getAddonInfo('fanart')

        def _info_image(cls):
            cls.info_image = os.path.join(__addon__.getAddonInfo('path'), 'resources', 'media', 'info.png')

        def _warning_image(cls):
            cls.warning_image = os.path.join(__addon__.getAddonInfo('path'), 'resources', 'media', 'warning.png')

        def _error_image(cls):
            cls.error_image = os.path.join(__addon__.getAddonInfo('path'), 'resources', 'media', 'error.png')

        def _limit(cls):
            cls.limit = 20

        def _last_update_id(cls):
            cls.last_update_id = __addon__.getSetting("last_update_id")

        def _fsencoding(cls):
            cls.fsencoding = sys.getfilesystemencoding() or 'utf-8'
