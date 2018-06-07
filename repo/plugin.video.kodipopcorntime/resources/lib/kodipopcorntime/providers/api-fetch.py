import os, sys, json, xbmc
import urllib2, re
from kodipopcorntime import settings
from kodipopcorntime.logging import log, LOGLEVEL
__addon__ = sys.modules['__main__'].__addon__

_categories = {
    '30350': 'Movies',
    '30351': 'TVShows',
    '30352': 'Anime'
}

_genres_movies_shows = {
    '30400': 'Action',
    '30401': 'Adventure',
    '30402': 'Animation',
    '30403': 'Comedy',
    '30404': 'Crime',
    '30405': 'Disaster',
    '30406': 'Documentary',
    '30407': 'Drama',
    '30408': 'Eastern',
    '30409': 'Family',
    '30410': 'Fan-Film',
    '30411': 'Fantasy',
    '30412': 'Film-Noir',
    '30413': 'History',
    '30414': 'Horror',
    '30415': 'Indie',
    '30416': 'Music',
    '30417': 'Mystery',
    '30418': 'Road',
    '30419': 'Romance',
    '30420': 'Science-Fiction',
    '30421': 'Short',
    '30422': 'Sports',
    '30423': 'Sporting-event',
    '30424': 'Suspence',
    '30425': 'Thriller',
    '30426': 'TV-Movie',
    '30427': 'War',
    '30428': 'Western'
}

_genres_anime = {
  '30450': 'Action',
  '30451': 'Ecchi',
  '30452': 'Harem',
  '30453': 'Romance',
  '30454': 'School',
  '30455': 'Supernatural',
  '30456': 'Drama',
  '30457': 'Comedy',
  '30458': 'Mystery',
  '30459': 'Police',
  '30461': 'Sports',
  '30462': 'Mecha',
  '30463': 'Sci-Fi',
  '30464': 'Slice+of+Life',
  '30465': 'Fantasy',
  '30466': 'Adventure',
  '30467': 'Gore',
  '30468': 'Music',
  '30469': 'Psychological',
  '30470': 'Shoujo+Ai',
  '30471': 'Yuri',
  '30472': 'Magic',
  '30473': 'Horror',
  '30474': 'Thriller',
  '30475': 'Gender+Bender',
  '30476': 'Parody',
  '30477': 'Historical',
  '30478': 'Racing',
  '30479': 'Samurai',
  '30480': 'Super+Power',
  '30481': 'Military',
  '30482': 'Dementia',
  '30483': 'Mahou+Shounen',
  '30484': 'Game',
  '30485': 'Martial+Arts',
  '30486': 'Vampire',
  '30487': 'Kids',
  '30488': 'Mahou+Shoujo',
  '30489': 'Space',
  '30490': 'Shounen+Ai'
}

_proxy_identifier = 'api-fetch.proxies'
def _getDomains():
    domains = [
        # Currently working and has all 3 categories
        "https://api-fetch.website"
    ]

    # User domains have highest priority
    return settings.movies.proxies+domains

def _create_item(data):
    if not data.get("title"): # Title is require
        return {}

    torrents = {}
    for torrent in data.get('torrents').get('en'):
        if torrent in settings.QUALITIES:
            torrents['%s' %torrent] = data.get('torrents').get('en').get('%s' %torrent).get('url')
            torrents['%ssize' %torrent] = data.get('torrents').get('en').get('%s' %torrent).get('size')

    # Do not show Movies without torrents
    if not torrents:
        return {}

    # Set video width and hight
    width = 1920
    height = 1080
    if not torrents.get('1080p'):
        width = 1280
        height = 720
    elif not torrents.get('720p'):
        width = 640
        height = 480

    title = data["title"]

    if data.get("trailer"):
        trailer_regex = re.match('^[^v]+v=(.{11}).*', data.get("trailer"))
        try:
            trailer_id = trailer_regex.group(1)
            log("(trailer) %s" %trailer_id, LOGLEVEL.INFO)
            trailer = "plugin://plugin.video.youtube/?action=play_video&videoid=%s" %trailer_id
        except:
            trailer = ''
            pass

    return {
        "label": title,
        "icon": data.get('images').get('poster'),
        "thumbnail": data.get('images').get('poster'),
        "info": {
            "title": title,
            "year": int(data.get("year") or 0),
            "genre": u" / ".join(genre for genre in data.get("genres", [])) or None,
            "duration": int(0),
            "code": data.get("imdb_id"),
            "trailer": trailer
        },
        "properties": {
            "fanart_image": data.get('images').get('fanart')
        },
        "stream_info": {
            "video": {
                "codec": u"h264",
                "duration": int(0),
                "width": width,
                "height": height
            },
            "audio": {
                "codec": u"aac",
                "language": u"en",
                "channels": 2
            }
        },
        "params": torrents
    }

def _create_shows_item(data):
    label = 'Episode %s: %s' % (data[0]['episode'], data[0]['title'])

    # seasondata0 has all the data from show
    seasondata0 = int(data[0]['season'])

    # seasondata_1 carries additional user data not included in show data
    seasondata_1 = int(data[-1]['seasons'])
    if not seasondata0 == seasondata_1:
        return {}

    # Do not return Shows  without torrents
    torrents = {}
    for torrent in data[0].get('torrents'):
        if torrent in settings.QUALITIES and data[0].get('torrents').get('%s' %torrent).get('url') != None:
            torrents['%s' %torrent] = data[0].get('torrents').get('%s' %torrent).get('url')
            torrents['%ssize' %torrent] = 1000000000*60
    if not torrents:
        return {}

    # Set video width and hight
    width = 1920
    height = 1080
    if not torrents.get('1080p'):
        width = 1280
        height = 720
    elif not torrents.get('720p'):
        width = 640
        height = 480

    return {
        "label": label,
        "icon": data[-1]['image'],
        "thumbnail": data[-1]['image'],
        "info": {
            "title": data[0]['title'],
            "year": int(data[0].get("year") or 0),
            "genre": u" / ".join(genre for genre in data[0].get("genres", [])) or None,
            "duration": int(0),
            "code": data[0].get("tvdb_id")
        },
        "properties": {
            "fanart_image": data[-1]['image2']
        },
        "stream_info": {
            "video": {
                "codec": u"h264",
                "duration": int(0),
                "width": width,
                "height": height
            },
            "audio": {
                "codec": u"aac",
                "language": u"en",
                "channels": 2
            }
        },
        "params": torrents
    }

def folders(action, **kwargs):
    '''folders are used to create lists of genres, shows, animes and seasons
       :param action: (string) When index is call, this parameter will be empty, then set an operation.
       :param kwargs: (dict) When index is call, this parameter will be empty, then contains the user parameters.
       :return: (list) Return a list with items. (Only the first item are used when index is call.)
    '''
    log("(api-fetch-folders) %s" %action, LOGLEVEL.INFO)
    if action == 'categories':
        '''Action categories creates list of categories '''
        items= []
        for n in __addon__.getLocalizedString(30353).split(','):
            if _categories.get(n):
                path = os.path.join(settings.addon.resources_path, 'media', 'categories', '%s.png' %_categories[n])
                items.append({
                    "label": __addon__.getLocalizedString(int(n)),
                    "icon": path,
                    "thumbnail": path,
                    "params": {
                        "endpoint": "folders",                                  # endpoint is required
                        'action': "cat_%s" %_categories[n]                      # action carries an operation
                    }
                })
        return items

    if action == 'cat_Movies':
        '''Action cat_Movies creates a list of options for movies '''
        return [
            {
                # Search option
                "label": __addon__.getLocalizedString(30002),                   # "label" is required
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'search.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'search.png'),
                "params": {
                    "categ": "movies",                                          # "categ" is required when using browse as an endpoint
                    "endpoint": "search"                                        # "endpoint" is required
                }
            },
            {
                # Most Popular option
                "label": __addon__.getLocalizedString(30004),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'popular.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'popular.png'),
                "params": {
                    "categ": "movies",                                          # "categ" is required when using browse as an endpoint
                    "endpoint": "browse",                                       # "endpoint" is require
                    'action': "trending",                                       # Require when calling browse or folders (Action is used to separate the content)
                    'order': '-1'
                }
            },
            {
                # Recently Added Option
                "label": __addon__.getLocalizedString(30006),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'recently.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'recently.png'),
                "params": {
                    "categ": "movies",                                          # "categ" is required when using browse as an endpoint
                    "endpoint": "browse",                                       # "endpoint" is required
                    'action': "last_added",                                     # Require when calling browse or folders (Action is used to separate the content)
                    'order': '-1'
                }
            },
            {
                # Best Rated Option
                "label": __addon__.getLocalizedString(30005),                       # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "params": {
                    "categ": "movies",                                          # "categ" is required when using browse as an endpoint
                    "endpoint": "browse",                                       # "endpoint" is require
                    'action': "rating",                                         # Require when calling browse or folders (Action is used to separate the content)
                    'order': '-1'
                }
            },
            {
                # Sort by Title Option
                "label": __addon__.getLocalizedString(30025),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "params": {
                    "categ": "movies",                                          # "categ" is required when using browse as an endpoint
                    "endpoint": "browse",                                       # "endpoint" is require
                    'action': "title",                                          # Require when calling browse or folders (Action is used to separate the content)
                    'order': '1'
                }
            },
            {
                # Sort By Year
                "label": __addon__.getLocalizedString(30026),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "params": {
                    "categ": "movies",                                          # "categ" is required when using browse as an endpoint
                    "endpoint": "browse",                                       # "endpoint" is require
                    'action': "year",                                           # Require when calling browse or folders (Action is used to separate the content)
                    'order': '-1'
                }
            },
            {
                # Browse by Genre Option
                "label": __addon__.getLocalizedString(30003),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres.png'),
                "params": {
                    "endpoint": "folders",                                      # "endpoint" is require
                    'action': "genres_movies"                                   # Require when calling browse or folders (Action is used to separate the content)
                }
            }
        ]

    if action == 'genres_movies':
        '''Action genres_movies creates a list of genres'''
        items= []
        for n in __addon__.getLocalizedString(30499).split(','):
            if _genres_movies_shows.get(n):
                path = os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres', '%s.png' %_genres_movies_shows[n])
                items.append({
                    "label": __addon__.getLocalizedString(int(n)),              # "label" is require
                    "icon": path,
                    "thumbnail": path,
                    "params": {
                        "categ": "movies",                                      # "categ" is required when using browse as an endpoint
                        "endpoint": "browse",                                   # "endpoint" is require
                        'action': "genre",                                      # Require when calling browse or folders (Action is used to separate the content)
                        'genre': _genres_movies_shows[n],
                        'order': '-1'
                    }
                })
        return items

    if action == 'cat_TVShows':
        '''Action cat_TVShows creates a list of options for TV Shows '''
        return [
            {
                # Sarch Option
                "label": __addon__.getLocalizedString(30002),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'search.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'search.png'),
                "params": {
                    "act": "search",
                    'search': 'true',
                    'action': 'show-list',                                      # Require when calling browse or folders (Action is used to separate the content)
                    "endpoint": "folders",                                       # "endpoint" is require
                    'page': 1,
                    'genre': 'all'
                }
            },
            {
                # Most Popular Option
                "label": __addon__.getLocalizedString(30004),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'popular.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'popular.png'),
                "params": {
                    "endpoint": "folders",                                      # "endpoint" is require
                    'act': "trending",
                    'search': 'false',
                    'genre': 'all',
                    'page': 1,
                    'action': "show-list"                                       # Require when calling browse or folders (Action is used to separate the content)
                }
            },
            {
                # Last Updated Option
                "label": __addon__.getLocalizedString(30027),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'recently.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'recently.png'),
                "params": {
                    "action": "show-list",                                      # Require when calling browse or folders (Action is used to separate the content)
                    'search': 'false',
                    'genre': 'all',
                    'page': 1,
                    "endpoint": "folders",                                      # "endpoint" is require
                    'act': "updated"
                }
            },
            {
                # Best Rated Option
                "label": __addon__.getLocalizedString(30005),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "params": {
                    "action": "show-list",                                      # Require when calling browse or folders (Action is used to separate the content)
                    'search': 'false',
                    'genre': 'all',
                    'page': 1,
                    "endpoint": "folders",                                      # "endpoint" is require
                    'act': "rating"
                }
            },
            {
                # Sort by Title Option
                "label": __addon__.getLocalizedString(30025),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "params": {
                    "action": "show-list",                                      # Require when calling browse or folders (Action is used to separate the content)
                    'search': 'false',
                    'genre': 'all',
                    'page': 1,
                    "endpoint": "folders",                                      # "endpoint" is require
                    'act': "name"
                }
            },
            {
                # Sort by Year Option
                "label": __addon__.getLocalizedString(30026),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "params": {
                    "action": "show-list",                                      # Require when calling browse or folders (Action is used to separate the content)
                    'search': 'false',
                    'genre': 'all',
                    'page': 1,
                    "endpoint": "folders",                                      # "endpoint" is require
                    'act': "year"
                }
            },
            {
                # Browse by Genre Option
                "label": __addon__.getLocalizedString(30003),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres.png'),
                "params": {
                    "endpoint": "folders",                                      # "endpoint" is require
                    'action': "genres_TV-shows"                                 # Require when calling browse or folders (Action is used to separate the content)
                }
            }
        ]

    if action == 'genres_TV-shows':
        '''Action genres_movies creates a list of genres'''
        items = []
        for n in __addon__.getLocalizedString(30499).split(','):
            if _genres_movies_shows.get(n):
                path = os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres', '%s.png' %_genres_movies_shows[n])
                items.append({
                    "label": __addon__.getLocalizedString(int(n)),              # "label" is require
                    "icon": path,
                    "thumbnail": path,
                    "params": {
                        "action": "show-list",                                   # Require when calling browse or folders (Action is used to separate the content)
                        'search': 'false',
                        "endpoint": "folders",                                  # "endpoint" is require
                        'act': "genre",
                        'page': 1,
                        'genre': _genres_movies_shows[n]
                    }
                })
        return items

    if action == 'cat_Anime':
        '''Action cat_TVShows creates a list of options for TV Shows '''
        return [
            {
                # Search Option
                "label": __addon__.getLocalizedString(30002),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'search.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'search.png'),
                "params": {
                    "act": "search",
                    'search': 'true',
                    'action': 'anime-list',                                     # Require when calling browse or folders (Action is used to separate the content)
                    "endpoint": "folders",                                       # "endpoint" is require
                    'page': 1,
                    'genre': 'all'
                }
            },
            {
                # Best Rated Option
                "label": __addon__.getLocalizedString(30005),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "params": {
                    "action": "anime-list",                                     # Require when calling browse or folders (Action is used to separate the content)
                    'search': 'false',
                    'genre': 'all',
                    "endpoint": "folders",                                      # "endpoint" is require
                    'act': "rating",
                    'page': 1
                }
            },
            {
                # Sort by Title Option
                "label": __addon__.getLocalizedString(30025),            #Title           # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "params": {
                    "action": "anime-list",                                     # Require when calling browse or folders (Action is used to separate the content)
                    'search': 'false',
                    'genre': 'all',
                    "endpoint": "folders",                                      # "endpoint" is require
                    'act': "name",
                    'page': 1
                }
            },
            {
                # Sort by Year Option
                "label": __addon__.getLocalizedString(30026),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'rated.png'),
                "params": {
                    "action": "anime-list",                                     # Require when calling browse or folders (Action is used to separate the content)
                    'search': 'false',
                    'genre': 'all',
                    "endpoint": "folders",                                      # "endpoint" is require
                    'act': "year",
                    'page': 1
                }
            },
            {
                # Browse by Genre Option
                "label": __addon__.getLocalizedString(30003),                   # "label" is require
                "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres.png'),
                "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres.png'),
                "params": {
                    "endpoint": "folders",                                      # "endpoint" is require
                    'action': "genres_anime"                                    # Require when calling browse or folders (Action is used to separate the content)
                }
            }
        ]

    if action == 'genres_anime':
        '''Action genres_anime creates a list of genres'''
        items= []
        for n in __addon__.getLocalizedString(30498).split(','):
            if _genres_anime.get(n):
                path = os.path.join(settings.addon.resources_path, 'media', 'movies', 'genres', '%s.png' %_genres_anime[n])
                items.append({
                    "label": __addon__.getLocalizedString(int(n)),              # "label" is require
                    "icon": path,
                    "thumbnail": path,
                    "params": {
                        "action": "anime-list",                                 # Require when calling browse or folders (Action is used to separate the content)
                        'search': 'false',
                        "endpoint": "folders",                                  # "endpoint" is require
                        'act': "genre",
                        'genre': _genres_anime[n],
                        'page': 1
                    }
                })
        return items

    if action == 'show-list':
        '''Action show-list creates a list of TV Shows'''
        dom = _getDomains()

        page = kwargs['page']

        # Search Dialog
        if kwargs['search'] == 'true':
            log("(Search-TV-Shows) Getting search string")
            search_string = xbmc.getInfoLabel("ListItem.Property(searchString)")
            if not search_string:
                log("(Search-TV-Shows) Showing keyboard")
                keyboard = xbmc.Keyboard('', __addon__.getLocalizedString(30001), False)
                keyboard.doModal()
                if not keyboard.isConfirmed() or not keyboard.getText():
                    raise Abort()
                search_string = keyboard.getText()
                search_string=search_string.replace(' ', '+')
            log("(Search-TV-Shows) Returning search string '%s'" %search_string)
            search = '%s/tv/shows/1?keywords=%s' % (dom[0], search_string)
        else:
            search = '%s/tv/shows/%s?genre=%s&sort=%s' % (dom[0], page, kwargs['genre'], kwargs['act'])

        req = urllib2.Request(search, headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.66 Safari/537.36", "Accept-Encoding": "none"})
        response = urllib2.urlopen(req)
        shows = json.loads(response.read())
        items = []
        for show in shows:
            log("(api-fetch-folder-show-list) %s" %show, LOGLEVEL.INFO)
            items.append({
                "label": show['title'],                                         # "label" is require
                "icon": show.get('images').get('poster'),
                "thumbnail": show.get('images').get('poster'),
                "params": {
                    "seasons": show['num_seasons'],
                    "endpoint": "folders",                                      # "endpoint" is require
                    'action': "show-seasons",                                   # Require when calling browse or folders (Action is used to separate the content)
                    'imdb_id': show['imdb_id'],
                    'poster': show.get('images').get('poster'),
                    'fanart': show.get('images').get('fanart')
                }
            })

        # Next Page
        items.append({
            "label": 'Show more',                                               # "label" is require
            "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'more.png'),
            "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'more_thumbnail.png'),
            "params": {
                "endpoint": "folders",                                          # "endpoint" is require
                'action': "show-list",                                          # Require when calling browse or folders (Action is used to separate the content)
                'act': kwargs['act'],
                'genre': kwargs['genre'],
                'search': kwargs['search'],
                'page': int(page)+1
            }
        })

        return items

    if action == 'show-seasons':
        '''Action show-seasons creates a list of seasons for a TV Show'''
        items = []
        dom = _getDomains()
        search = '%s/tv/show/%s' % (dom[0], kwargs['imdb_id'])
        req = urllib2.Request(search, headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.66 Safari/537.36", "Accept-Encoding": "none"})
        response = urllib2.urlopen(req)
        result = json.loads(response.read())
        seasons = result['episodes']

        season_list = []

        for season in seasons:
            log("(api-fetch-folder-show-list) %s" %season, LOGLEVEL.INFO)
            season_list.append(season['season'])

        season_list2 = sorted(list(set(season_list)))

        for season2 in season_list2:
            log("(api-fetch-folder-show-list) %s" %season2, LOGLEVEL.INFO)
            items.append({
                "label": 'Season %s' %season2,                                  # "label" is require
                "icon": kwargs['poster'],
                "thumbnail": kwargs['poster'],
                "params": {
                    'categ': 'shows',                                           # "categ" is required when using browse as an endpoint
                    'seasons': season2,
                    'image': kwargs['poster'],
                    'image2':kwargs['fanart'],
                    "endpoint": "browse",                                       # "endpoint" is require
                    'action': kwargs['imdb_id']                                 # Require when calling browse or folders (Action is used to separate the content)
                }
            })
        return items

    if action == 'anime-list':
        '''Action anime-list creates a list of Animes'''
        dom = _getDomains()

        if kwargs['search'] == 'true':
            log("(Search-Animes) Getting search string")
            search_string = xbmc.getInfoLabel("ListItem.Property(searchString)")
            if not search_string:
                log("(Search-Animes) Showing keyboard")
                keyboard = xbmc.Keyboard('', __addon__.getLocalizedString(30001), False)
                keyboard.doModal()
                if not keyboard.isConfirmed() or not keyboard.getText():
                    raise Abort()
                search_string = keyboard.getText()
                search_string = search_string.replace(' ', '+')
            log("(Search-Animes) Returning search string '%s'" %search_string)
            search = '%s/tv/animes/1?keywords=%s' % (dom[0], search_string)
        else:
            search = '%s/tv/animes/%s?genre=%s&sort=%s' % (dom[0], kwargs['page'], kwargs['genre'], kwargs['act'])

        req = urllib2.Request(search, headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.66 Safari/537.36", "Accept-Encoding": "none"})
        response = urllib2.urlopen(req)
        animes = json.loads(response.read())

        items = []
        for anime in animes:
            log("(api-fetch-folder-show-list) %s" %anime, LOGLEVEL.INFO)
            items.append({
                "label": anime['title'],                                        # "label" is require
                "icon": anime.get('images').get('poster'),
                "thumbnail": anime.get('images').get('poster'),
                "params": {
                    "endpoint": "folders",                                      # "endpoint" is require
                    'action': "anime-seasons",                                  # Require when calling browse or folders (Action is used to separate the content)
                    '_id': anime['_id'],
                    'poster': anime.get('images').get('poster'),
                    'fanart': anime.get('images').get('fanart')
                }
            })

        # Next Page
        items.append({
            "label": 'Show more',                                               # "label" is require
            "icon": os.path.join(settings.addon.resources_path, 'media', 'movies', 'more.png'),
            "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies', 'more_thumbnail.png'),
            "params": {
                "endpoint": "folders",                                          # "endpoint" is require
                'action': "anime-list",                                          # Require when calling browse or folders (Action is used to separate the content)
                'act': kwargs['act'],
                'genre': kwargs['genre'],
                'search': kwargs['search'],
                'page': int(kwargs['page'])+1
            }
        })

        return items

    if action == 'anime-seasons':
        '''Action anime-seasons creates a list of seasons for a Animes'''
        items = []
        dom = _getDomains()
        search = '%s/tv/anime/%s' % (dom[0], kwargs['_id'])

        req = urllib2.Request(search, headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.66 Safari/537.36", "Accept-Encoding": "none"})
        response = urllib2.urlopen(req)
        result = json.loads(response.read())

        seasons = result['episodes']

        season_list = []
        for season in seasons:
            season_list.append(season['season'])

        season_list2 = sorted(list(set(season_list)))

        for season2 in season_list2:
            log("(api-fetch-folder-anime-list) %s" %season2, LOGLEVEL.INFO)
            items.append({
                "label": 'Season %s' %season2,                                  # "label" is require
                "icon": kwargs['poster'],
                "thumbnail": kwargs['poster'],
                "params": {
                    'categ': 'anime',                                           # "categ" is required when using browse as an endpoint
                    'seasons': season2,
                    'image': kwargs['poster'],
                    'image2':kwargs['fanart'],
                    "endpoint": "browse",                                       # "endpoint" is require
                    'action': kwargs['_id']                                     # Require when calling browse or folders (Action is used to separate the content)
                }
            })
        return items

    # There was no action, therefore has index be called
    return [{
        "label": __addon__.getLocalizedString(30030),                               # "label" is require
        "icon": os.path.join(settings.addon.resources_path, 'media', 'movies.png'),
        "thumbnail": os.path.join(settings.addon.resources_path, 'media', 'movies.png'),
        "params": {
            "endpoint": "folders",                                                  # "endpoint" is require
            'action': "categories"                                                         # Require when calling browse or folders (Action is used to separate the content)
        }
    }]

def browse(action, page, **kwargs):
    '''browse are used to returning parameters used for 'Request' when a movie list is displayed.
       :param action: (string) This parameter set an operation
       :param page: (int) Contains the current page number
       :param kwargs: (dict) Contain user parameters
       :return: (dict) Return parameters used for 'Request'
    '''

    if kwargs['categ'] == 'movies':
        return {
            'proxies': _getDomains(),
            'path': "/tv/movies/%s" %page,
            'params': {
                'genre': action == 'genre' and kwargs['genre'] or 'all',
                'sort': action == 'genre' and "seeds" or action,
                'order': kwargs['order']
            },
            'proxyid': _proxy_identifier
        }
    if kwargs['categ'] == 'shows':
        return {
            'proxies': _getDomains(),
            'path': "/tv/show/%s" %action,
            'params': {
            },
            'proxyid': _proxy_identifier
        }
    if kwargs['categ'] == 'anime':
        return {
            'proxies': _getDomains(),
            'path': "/tv/anime/%s" %action,
            'params': {
            },
            'proxyid': _proxy_identifier
        }
    else:
        return {}

def browse_build(data, action, page, **kwargs):
    '''browse_build are used to create a dict with the items when a movie list is displayed.

       :param data: Contains a list with data from 'Request'
       :param action: (string) This parameter set an operation
       :param page: (int) Contains the current page number
       :param kwargs: (dict) Contain user parameters that were given to browse function
       :return: Return a dict
    '''
    items = []

    if kwargs['categ'] == 'movies':
        for movie in data:
            item = _create_item(movie)
            if item:
                items.append(item)
        if not items:
            return {}
    elif kwargs['categ'] == 'shows':
        episodes = data['episodes']
        for episode in episodes:
            episode2 = []
            episode2.append(episode)
            episode2.append(kwargs)
            item = _create_shows_item(episode2)
            if item:
                items.append(item)
        if not items:
            return {}
    elif kwargs['categ'] == 'anime':
        episodes = data['episodes']
        for episode in episodes:
            episode2 = []
            episode2.append(episode)
            episode2.append(kwargs)
            item = _create_shows_item(episode2)
            if item:
                items.append(item)
        if not items:
            return {}
    else:
        return {}

    return {
        'pages': 50, #int(movie_count/settings.addon.limit) + (movie_count%settings.addon.limit > 0), # Specify the total number of pages (require)
        'items': items
    }

def search(query, page, **kwargs):
    '''search are used to returning parameters used for 'Request' when a search result is displayed.

       :param query: (string) Contains an query string
       :param page: (int) Contains the current page number
       :param kwargs: (dict) Contain user parameters
       :return: (dict) Return parameters used for 'Request'
    '''
    if kwargs['categ'] == 'movies':
        return {
            'proxies': _getDomains(),
            'path': "/tv/movies/%s" %page,
            'params': {
                'page': page,
                'quality': 'all',
                'keywords': query.encode('UTF-8')
            },
        'proxyid': _proxy_identifier
        }
    else:
        return {}

def search_build(data, query, page, **kwargs):
    '''search_build are used to create a dict with the items when a search result is displayed.

       :param data: Contains a list with data from 'Request'
       :param query: (string) Contains an query string
       :param page: (int) Contains the current page number
       :param kwargs: (dict) Contain user parameters that were given to search function
       :return: Return a dict
    '''
    items = []
    for movie in data:
        item = _create_item(movie)
        if item:
            items.append(item)
    if not items:
        return {}

    return {
        'pages': 50,
        'items': items
    }
