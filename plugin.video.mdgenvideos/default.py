import sys,urllib,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,json
import requests
from addon.common.addon import Addon
from addon.common.net import Net
from metahandler import metahandlers

#GenVideos Add-on Created By Mucky Duck (2/2016)

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.mdgenvideos'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
metaset = selfAddon.getSetting('enable_meta')
metaget = metahandlers.MetaData()
baseurl = 'http://genvideos.org'
net = Net()




def CAT():
        addDir('[B][COLOR white]Popular Movies[/COLOR][/B]',baseurl,1,icon,fanart,'')
        addDir('[B][COLOR white]Recent Movies[/COLOR][/B]',baseurl+'/recent_movies',1,icon,fanart,'')
        addDir('[B][COLOR white]Most Viewed[/COLOR][/B]',baseurl+'/most_viewed',1,icon,fanart,'')
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',4,icon,fanart,'')
        addDir('[B][COLOR white]Genre[/COLOR][/B]',baseurl,2,icon,fanart,'')
        addDir('[B][COLOR white]Year[/COLOR][/B]',baseurl,5,icon,fanart,'')




def INDEX(url):
        link = OPEN_URL(url)
        all_videos = regex_get_all(link, 'cell_container', '<div><b>')
        items = len(all_videos)
        for a in all_videos:
                name = regex_from_to(a, 'a title="', '\(')
                name = addon.unescape(name)
                url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
                thumb = regex_from_to(a, 'src="', '"')
                if metaset=='true':
                        addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,baseurl+url,3,'http://'+thumb,items)
                else:
                        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,baseurl+url,3,'http://'+thumb,fanart,'')
        try:
                match = re.compile('<a href="(.*?)\?page\=(.*?)">').findall(link)
                for url, pn in match:
                        url = baseurl+url+'?page='+pn
                        addDir('[I][B][COLOR red]Page %s >>>[/COLOR][/B][/I]' %pn,url,1,icon,fanart,'')
        except: pass
        setView('movies', 'movie-view')




def LINK(url):
        url = re.split(r'#', url, re.I)[0]
        request_url = baseurl+'/video_info/iframe'
        link = OPEN_URL(url)
        form_data={'v': re.search(r'v\=(.*?)$',url,re.I).group(1)}
        headers = {'origin':'http://genvideos.org', 'referer': url,
                   'user-agent':baseurl,'x-requested-with':'XMLHttpRequest'}
        r = requests.post(request_url, data=form_data, headers=headers)
        try:
                url = re.findall(r'url\=(.*?)"', str(r.text), re.I|re.DOTALL)[-1]
        except:
                url = re.findall(r'url\=(.*?)"', str(r.text), re.I|re.DOTALL)[0]
        url = url.replace("&amp;","&").replace('%3A',':').replace('%3D','=').replace('%2F','/')
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setInfo(type='Video', infoLabels={'Title':description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(str(url))
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)




def SEARCH():
        keyb = xbmc.Keyboard('', 'Search')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','+')
                url = baseurl+'/results?q='+search
                INDEX(url)




def GENRE(url):
        link = OPEN_URL(url)
        all_links = regex_get_all(link, 'Genres<', '</ul>')
        all_videos = regex_get_all(str(all_links), '<li>', '</li>')
        for a in all_videos:
                name = regex_from_to(a, '<span>', '</span>')
                url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,baseurl+url,1,icon,fanart,'')




def YEAR(url):
        link = OPEN_URL(url)
        all_links = regex_get_all(link, 'years<', '</ul>')
        all_videos = regex_get_all(str(all_links), '<li>', '</li>')
        for a in all_videos:
                name = regex_from_to(a, '<span>', '</span>')
                url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,baseurl+url,1,icon,fanart,'')
                




def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param




def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name,"Plot":description} )
        liz.setProperty('fanart_image', fanart)
        if mode==3:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok




def PT(url):
        addon.log('Play Trailer %s' % url)
        notification( addon.get_name(), 'fetching trailer', addon.get_icon())
        xbmc.executebuiltin("PlayMedia(%s)"%url)




def notification(title, message, icon):
        addon.show_small_popup( addon.get_name(), message.title(), 5000, icon)
        return




def addDir2(name,url,mode,iconimage,itemcount):
        name = name.replace('[B][COLOR white]','').replace('[/COLOR][/B]','')
        meta = metaget.get_meta('movie',name)
        if meta['cover_url']=='':
            try:
                meta['cover_url']=iconimage
            except:
                meta['cover_url']=icon
        name = '[B][COLOR white]' + name + '[/COLOR][/B]'
        meta['title'] = name
        contextMenuItems = []
        if meta['trailer']>'':
                contextMenuItems.append(('Play Trailer', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'mode': 6, 'url':meta['trailer']})))
        contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
        liz.setInfo( type="Video", infoLabels= meta )
        liz.addContextMenuItems(contextMenuItems, replaceItems=False)
        if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
        else: liz.setProperty('fanart_image', fanart)
        if mode==3:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False,totalItems=itemcount)
        else:
             ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True,totalItems=itemcount)
        return ok




def addLink(name,url,mode,iconimage,fanart,description=''):
        #u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        #ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok




def OPEN_URL(url):
    headers = {}
    headers['User-Agent'] = User_Agent
    link = requests.get(url, headers=headers).text
    link = link.encode('ascii', 'ignore').decode('ascii')
    return link




def regex_from_to(text, from_string, to_string, excluding=True):
        if excluding:
                try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
                except: r = ''
        else:
                try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
                except: r = ''
        return r




def regex_get_all(text, start_with, end_with):
        r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
        return r




''' Why recode whats allready written and works well,
    Thanks go to Eldrado for it '''

def setView(content, viewType):
        
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if addon.get_setting('auto-view') == 'true':

        print addon.get_setting(viewType)
        if addon.get_setting(viewType) == 'Info':
            VT = '504'
        elif addon.get_setting(viewType) == 'Info2':
            VT = '503'
        elif addon.get_setting(viewType) == 'Info3':
            VT = '515'
        elif addon.get_setting(viewType) == 'Fanart':
            VT = '508'
        elif addon.get_setting(viewType) == 'Poster Wrap':
            VT = '501'
        elif addon.get_setting(viewType) == 'Big List':
            VT = '51'
        elif viewType == 'default-view':
            VT = addon.get_setting(viewType)

        print viewType
        print VT
        
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ( int(VT) ) )

    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_MPAA_RATING )




params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None



try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:
        description=urllib.unquote_plus(params["description"])
except:
        pass




if mode==None or url==None or len(url)<1:
        CAT()

elif mode==1:
        INDEX(url)

elif mode==2:
        GENRE(url)

elif mode==3:
        LINK(url)

elif mode==4:
        SEARCH()

elif mode==5:
        YEAR(url)

elif mode==6:
        PT(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
