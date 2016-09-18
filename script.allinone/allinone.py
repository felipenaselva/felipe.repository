import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmc

import urllib
import urllib2

import sys
import re
import os

import utils


repo      = xbmc.translatePath(os.path.join('special://home', 'addons', 'repository.*'))
addonpath = xbmc.translatePath(os.path.join('special://home', 'addons'))


global APPLICATION


PLUGIN   = utils.PLUGIN
VIDEO    = utils.VIDEO
AUDIO    = utils.AUDIO
EXEC     = utils.EXEC
PICTURE  = utils.PICTURE
SETTINGS = utils.SETTINGS


VIDEO_IMG   = utils.VIDEO_IMG
MUSIC_IMG   = utils.MUSIC_IMG
PROGRAM_IMG = utils.PROGRAM_IMG
PICTURE_IMG = utils.PICTURE_IMG


def Categories():
    addDir('Video',    '', mode=VIDEO,   iconimage=VIDEO_IMG,   description='Show Video addons',   isFolder=True, fanart=VIDEO_IMG,   type='VIDEO')
    addDir('Audio',    '', mode=AUDIO,   iconimage=MUSIC_IMG,   description='Show Audio addons',   isFolder=True, fanart=MUSIC_IMG,   type='AUDIO')
    addDir('Programs', '', mode=EXEC,    iconimage=PROGRAM_IMG, description='Show Program addons', isFolder=True, fanart=PROGRAM_IMG, type='EXECECUTABLE')
    addDir('Pictures', '', mode=PICTURE, iconimage=PICTURE_IMG, description='Show Picture addons', isFolder=True, fanart=PICTURE_IMG, type='PICTURE')
 
    
def GetCategories(category=None):
     import glob

     items   = []
     plugins = {}

     if category:
         category = category.lower()

     for infile in glob.glob(repo):
         if 'repository.superrepo' in infile.lower():
             continue
             

         file    = os.path.join(infile, 'addon.xml')
         link    = open(file).read()

         fullist = re.compile('<info compressed=".+?">(.+?)</info>').findall(link)[0]
         datadir = re.compile('<datadir zip=".+?">(.+?)</datadir>').findall(link)[0] + '/'

         html    = OPEN_URL(fullist)
         html    = html.split('<addon ')

         for p in html:             
             try:
                 plugin = re.compile('id="(.+?)"').findall(p)[0]
                 author = re.compile('provider-name="(.+?)"').findall(p)[0]

                 pLower = plugin.lower()

                 if pLower in plugins and plugins[pLower] == author:
                     continue

                 plugins[pLower] = author

                 name      = re.compile(' name="(.+?)"').findall(p)[0].replace('*','')

                 author = utils.Clean(author)
                 name   = utils.Clean(name)

                 iconimage = os.path.join(datadir, plugin, 'icon.png')
                 fanart    = os.path.join(datadir, plugin, 'fanart.jpg')

                 try:    provides = re.compile('<provides>(.+?)</provides>').findall(p)[0]
                 except: provides = None

                 toAdd = False
                 if category == None:
                     toAdd = (provides != None)
                 else:
                     if provides:
                         toAdd = category in provides.lower()

                 if toAdd:
                     try:    desc = re.compile('<description lang="en">(.+?)<').findall(p)[0]
                     except: desc = ''                
                         
                     colour = '[COLOR grey]'
                     sort   = name

                     installed = os.path.exists(os.path.join(addonpath, plugin))
                     if installed:
                         iconimage = os.path.join(addonpath, plugin, 'icon.png')

                         if os.path.exists(os.path.join(addonpath, plugin, 'fanart.jpg')):
                             fanart = os.path.join(addonpath, plugin, 'fanart.jpg')

                         colour = '[COLOR white]'
                         sort   = '.' + name
                         
                     title = colour + name.upper() +'    -     [COLOR yellow]**[/COLOR]' + author.upper() + '[COLOR yellow]**[/COLOR]' + '[/COLOR]'

                     items.append([sort.lower(), title, plugin, PLUGIN, iconimage, desc, fanart])
             except:
                 pass 


     items.sort()

     isFolder = False
     for item in items:
         addDir(item[1], item[2], item[3], item[4], item[5], isFolder, item[6], type=category)
       
   
     
def GetContent(url,type):
    APPLICATION.closeBusy()

    ids = {}
    ids['10001'] = '10025'
    ids['10501'] = '10025'
    ids['10025'] = '10501'
    ids['10002'] = '10025'

    type = type.replace('executable', '10001')
    type = type.replace('audio',      '10501')
    type = type.replace('video',      '10025')
    type = type.replace('image',      '10002')   


    if type == xbmcgui.Window(10000).getProperty('SWIFT_LAUNCH_ID'):
        type = ids[type]

    cmd  = '%s,plugin://%s,return' % (type, url)
    xbmc.executebuiltin('ActivateWindow(%s)' % cmd)
    

               
def OPEN_URL(url):
    return utils.GetHTML(url)
   

def addDir(name, url, mode, iconimage, description, isFolder, fanart, type=''):
    u  = ''
    u += "?url="         + urllib.quote_plus(url)
    u += "&mode="        + str(mode)
    u += "&name="        + urllib.quote_plus(name)
    u += "&iconimage="   + urllib.quote_plus(iconimage)
    u += "&description=" + urllib.quote_plus(description)
    u += "&fanart="      + urllib.quote_plus(fanart)

    if len(type) > 0:
        u += "&type="    + urllib.quote_plus(type)

    infoLabels = {'title':name, 'fanart':fanart, 'description':description, 'thumb':iconimage}

    menu = []
    menu.append(('Settings', '?mode=%d' % SETTINGS))

    APPLICATION.addDir(name, mode, u, iconimage, isFolder=isFolder, isPlayable=False, infoLabels=infoLabels, contextMenu=menu, replaceItems=True)


def get_params(params):
    if not params:
        return {}

    param = {}

    cleanedparams = params.replace('?','')

    if (params[len(params)-1] == '/'):
       params = params[0:len(params)-2]

    pairsofparams = cleanedparams.split('&')    

    for i in range(len(pairsofparams)):
        splitparams = pairsofparams[i].split('=')

        if len(splitparams) == 2:
            param[splitparams[0]] = splitparams[1]

    return param


def main(params):    
    APPLICATION.showBusy()
    url         = None
    name        = None
    mode        = None
    iconimage   = None
    description = None
    fanart      = None
    type        = None


    try:    url = urllib.unquote_plus(params["url"])
    except: pass

    try:    name = urllib.unquote_plus(params["name"])
    except: pass

    try:    iconimage = urllib.unquote_plus(params["iconimage"])
    except: pass

    try:    mode = int(params["mode"])
    except: pass

    try:    description = urllib.unquote_plus(params["description"])
    except: pass

    try:    fanart = urllib.unquote_plus(params["fanart"])
    except: pass

    try:    type = urllib.unquote_plus(params["type"])
    except: pass


    if mode == PLUGIN:
        GetContent(url, type)


    elif mode == VIDEO:
        GetCategories('VIDEO')


    elif mode == AUDIO:
        GetCategories('AUDIO')


    elif mode == EXEC:
        GetCategories('EXECUTABLE')

    elif mode == PICTURE:
        GetCategories('IMAGE')


    elif mode == SETTINGS:
        APPLICATION.closeBusy()
        utils.openSettings()


    else:
        Categories()


    APPLICATION.closeBusy()


def onParams(application, params):
    global APPLICATION
    APPLICATION = application

    params = get_params(params)
    main(params)
