
#       Copyright (C) 2013-
#       Sean Poyser (seanpoyser@gmail.com)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import allinone
functionality = allinone

import xbmc
import xbmcgui
import xbmcaddon
import xbmcgui
import xbmcplugin
import os
import re
import urllib
import threading


import favourite

import utils

ACTION_SELECT     = 7
ACTION_PARENT_DIR = 9
ACTION_BACK       = 92
ACTION_LCLICK     = 100
ACTION_RCLICK     = 101
ACTION_CONTEXT    = 117

ESC = 61467

MAINLIST    = 59

VIDEO_BTN   = 3010
AUDIO_BTN   = 3020
EXEC_BTN    = 3030
PICTURE_BTN = 3040

LISTBACK  = -999

GETTEXT = utils.GETTEXT

PLUGIN   = utils.PLUGIN
VIDEO    = utils.VIDEO
AUDIO    = utils.AUDIO
EXEC     = utils.EXEC
PICTURE  = utils.PICTURE
SETTINGS = utils.SETTINGS

MAJOR, MINOR = utils.GetXBMCVersion()
       

class Application(xbmcgui.WindowXML):
    def __new__(cls, addonID):
        skin = utils.getSetting('SKIN')
        path = os.path.join(xbmcaddon.Addon(addonID).getAddonInfo('path'), 'resources', 'skins', skin)
        return super(Application, cls).__new__(cls, 'main.xml', path)


    def __init__(self, addonID):        
        super(Application, self).__init__()  

        self.ADDONID         = addonID
        self.ADDON           = xbmcaddon.Addon(self.ADDONID)
        self.skin            = utils.getSetting('SKIN')
        self.properties      = {}        
        self.lists           = []
        self.start           = None        
        self.context         = False
        self.busy            = None
        self.showBack        = False
        self.timer           = None
        self.mode            = 0
        self.faves           = str(favourite.getFavourites())
        self.fullScreenCount = 0
        self.footerCount     = 0
        self.setProperty('LB_FOOTER',  '')


    def onInit(self): 
        if self.start:            
            self.lists.append([]) 
            start      = self.start
            self.start = None
            self.onParams(start)
            return
            
        if len(self.lists) < 1:   
            if self.getTheme() == 'icons':
                self.setMode(self.getMode())
            else:
                self.onParams('init')
            return

        #add new list so we can just call onBack        
        self.newList()
        self.onBack()         


    def run(self, param=''):        
        self.start = param

        if self.start and self.start.startswith('_Playable'):
            #this will be a Playable item called from Favourites menu
            self.newList()
            self.windowed = False
            self.onParams(self.start.replace('_Playable', ''), isFolder=False)
            return

        #self.resetTimer()
        self.doModal()

              
    def close(self):
        xbmcgui.Window(10000).clearProperty('SWIFT_LAUNCH_ID')
        self.stopTimer()
        xbmcgui.WindowXML.close(self)


    def resetTimer(self):
        try:
            self.stopTimer()
            self.timer = threading.Timer(1, self.onTimer) 
            self.timer.start()
        except Exception, e:
            pass
        

    def stopTimer(self):
        if not self.timer:
            return

        try:
            self.timer.cancel()        
            del self.timer
            self.timer = None
        except Exception, e:
            pass


    def onTimer(self):
        self.resetTimer()


    def checkSkin(self):
        skin = utils.getSetting('SKIN')

        if self.skin == skin:
            self.inCheckSkin = False
            return

        self.skin = skin

        utils.Launch()
        self.close()


    def onFocus(self, controlId):
         utils.Log('onFocus %d' % controlId)

         if controlId == VIDEO_BTN:
             self.setMode(VIDEO)

         if controlId == AUDIO_BTN:
             self.setMode(AUDIO)

         if controlId == EXEC_BTN:
             self.setMode(EXEC)

         if controlId == PICTURE_BTN:
             self.setMode(PICTURE)

    def onAction(self, action):
        #see here https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h for the full list

        actionId = action.getId()
        buttonId = action.getButtonCode()

        if actionId != 107:
            utils.Log('onAction actionID %d' % actionId)
            utils.Log('onAction buttonID %d' % buttonId)

        if actionId in [ACTION_CONTEXT, ACTION_RCLICK]:
            return self.onContextMenu()
            
        if actionId in [ACTION_PARENT_DIR, ACTION_BACK] or buttonId in [ESC]:
            return self.onBack()        

        try:    id = self.getFocus().getId()         
        except: id = 0

        select = (actionId == ACTION_SELECT) or (actionId == ACTION_LCLICK)

        if select and id == MAINLIST:   
            liz        = self.getSelectedItem()
            param      = liz.getProperty('Param')
            image      = liz.getProperty('Image')
            mode       = int(liz.getProperty('Mode'))
            isFolder   = liz.getProperty('IsFolder')   == 'true'
            isPlayable = liz.getProperty('IsPlayable') == 'true'

            if mode == LISTBACK:
                return self.onBack()

            if param:
                self.stopTimer()
                self.onParams(param, isFolder)
                self.resetTimer()
        
                                 
    def onClick(self, controlId):        
        utils.Log('onClick %d' % controlId)

        if controlId == VIDEO_BTN:
            self.setMode(VIDEO)

        if controlId == AUDIO_BTN:
            self.setMode(AUDIO)

        if controlId == EXEC_BTN:
            self.setMode(EXEC)

        if controlId == PICTURE_BTN:
            self.setMode(PICTURE)


    def onBack(self): 
        self.lists.pop()
        if len(self.lists) == 0:
            self.close()
            return

        self.list = self.lists[-1]

        if len(self.list) == 0:
            #addon must have originally been started with a
            #parameter therefore reset to initial position
            self.lists = []
            self.onInit()
            return
            
        if hasattr(functionality, 'onBack'):
           functionality.onBack(self, self.list[0])
           
        self.addItems(self.list)
            
            
    def onContextMenu(self):
        if self.context:            
            return
        
        liz   = self.getSelectedItem()        
        index = int(liz.getProperty('Index'))
        item  = self.list[index]
        menu  = item['ContextMenu']

        replaceItems = liz.getProperty('ReplaceItems') == 'true'
        
        if not replaceItems:
            menu = list(menu + self.getSTDMenu(liz))            

        if len(menu) < 1:
            return

        import contextmenu
        self.context = True
        params       = contextmenu.showMenu(self.ADDONID, menu)
        self.context = False

        if not params:
            return

        if self.trySTDMenu(params):
            return
           
        self.onParams(params, isFolder=False)
        

    def showControl(self, id, show):
        try:    self.getControl(id).setVisible(show)
        except: pass
        
        
    def getProgress(self):
        try:    return self.busy.getControl(10)
        except: return None
        
        
    def showBusy(self):
        self.busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
        self.busy.show()
        progress = self.getProgress()
        if progress:
            progress.setVisible(False)        
        
        
    def closeBusy(self):    
        if self.busy:
            self.busy.close()
            self.busy = None


    def getTheme(self):
        return utils.getSetting('SKIN').lower()


    def getMode(self):
        try:    mode = int(utils.getSetting('MODE'))
        except: mode = VIDEO

        return mode 


    def setMode(self, mode):
        utils.setSetting('MODE', str(mode))

        if self.mode == mode:
            return

        self.mode = mode

        self.refreshModeControls()

        self.lists = []
        params = '?mode=%d' % self.mode
        self.onParams(params)


    def refreshModeControls(self):
        root = 4000
        self.getControl(root+100).setVisible(self.mode == 100)
        self.getControl(root+200).setVisible(self.mode == 200)
        self.getControl(root+300).setVisible(self.mode == 300)
        self.getControl(root+400).setVisible(self.mode == 400)


    def newList(self):
        self.list = []
        self.lists.append(self.list)        


    def getSelectedItem(self):
        try:    return self.getListItem(self.getCurrentListPosition())
        except: return None


    def setControlImage(self, id, image):
        if image == None:
            return

        control = self.getControl(id)
        if not control:
            return

        if 'http' in image:
            image = image.replace(' ', '%20')

        try:    control.setImage(image)
        except: pass

            
    def clearList(self): 
        if MAJOR < 13:
            self.showControl(MAINLIST, False)      
            for i in range(self.getListSize(), 0, -1):            
                self.removeItem(i-1)
            self.showControl(MAINLIST, True)
            return

        xbmcgui.WindowXML.clearList(self)  


    def getSTDMenu(self, liz):
        param = liz.getProperty('Param')

        std = []

        if param in self.faves:
            std.append(('Remove from favourites', 'STD:REMOVEFAVOURITE'))
        else:
            std.append(('Add to favourites',      'STD:ADDFAVOURITE'))

        std.append(('Add-on settings', 'STD:SETTINGS'))
        return std


    def trySTDMenu(self, params):

        if params == 'STD:SETTINGS':
            self.addonSettings()
            return

        if params == 'STD:ADDFAVOURITE':
            return self.addFavourite()

        if params == 'STD:REMOVEFAVOURITE':
            return self.removeFavourite()

        return False


    def addFavourite(self):
        liz        = self.getSelectedItem()
        name       = liz.getLabel()
        param      = liz.getProperty('Param')
        thumb      = liz.getProperty('Image')
        isPlayable = liz.getProperty('IsPlayable') == 'true'

        self.faves += param

        if isPlayable:
            param = '_Playable' + param
 
        cmd = 'RunScript(%s,%s)' % (self.ADDONID, param)

        favourite.add(name, cmd, thumb)

        return True


    def removeFavourite(self):
        liz   = self.getSelectedItem()
        param = liz.getProperty('Param')

        self.faves = self.faves.replace(param, '')

        return True


    def addonSettings(self):
        self.ADDON.openSettings()
        return True
        
        
    def setProperty(self, property, value):
        self.properties[property] = value
        xbmcgui.Window(10000).setProperty(property, value)
        
        
    def clearProperty(self, property):
        del self.properties[property]
        xbmcgui.Window(10000).clearProperty(property)        
        
        
    def clearAllProperties(self):
        for property in self.properties:
            xbmcgui.Window(10000).clearProperty(property)
            
        self.properties = {}        


    def addDir(self, name, mode, url='', image=None, isFolder=True, isPlayable=False, totalItems=0, contextMenu=[], replaceItems=False, infoLabels={}):
        if not image:
            image = ''

        if not contextMenu:
            contextMenu=[]

        if not infoLabels:
            infoLabels={}

        item = {}
        item['Name']         = name
        item['Mode']         = mode
        item['Url']          = url
        item['Image']        = image
        item['IsFolder']     = isFolder
        item['IsPlayable']   = isPlayable
        item['ContextMenu']  = contextMenu
        item['ReplaceItems'] = replaceItems
        item['InfoLabels']   = infoLabels

        self.list.append(item)
        
        progress = self.getProgress()
        if not progress:
            return
            
        if totalItems == 0:
            progress.setVisible(False)
        else:
            progress.setVisible(True)
            nItems = float(len(self.list) - 1) # subtract params'
            if self.showBack:
                nItems -= 1 # subtract params' and 'back' items
            perc   = 100 * nItems / totalItems            
            progress.setPercent(perc)   
        

    def addItems(self, theList):  
        self.clearList()
        self.showControl(MAINLIST, False)   
                        
        ignore = True
        index  = 1 #not '0' because first item in list is the params item
        
        for item in theList:
            if ignore:
                ignore = False
                continue
                
            name         = item['Name']
            mode         = item['Mode']
            url          = item['Url']
            image        = item['Image']
            isFolder     = item['IsFolder']
            isPlayable   = item['IsPlayable']
            contextMenu  = item['ContextMenu']
            replaceItems = item['ReplaceItems']
            infoLabels   = item['InfoLabels']

            liz = xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)

            liz.setProperty('Index',        str(index))
            liz.setProperty('Mode',         str(mode))
            liz.setProperty('Param',        url)
            liz.setProperty('Image',        image)
            liz.setProperty('IsFolder',     'true'  if isFolder     else 'false')
            liz.setProperty('IsPlayable',   'true'  if isPlayable   else 'false')
            liz.setProperty('ReplaceItems', 'true'  if replaceItems else 'false')

            index += 1

            if contextMenu and (len(contextMenu) > 0):
                #doesn't seem to work for script plugins??
                #but we'll set it anyway
                liz.addContextMenuItems(contextMenu)
  
            if infoLabels and (len(infoLabels) > 0):
                liz.setInfo(type='', infoLabels=infoLabels)
                #each infolabel is set as a property, this allow user-defined infoLabels
                #that can be accessed in the skin xml via: $INFO[Window.Property(USERDEFINED)]
                for item in infoLabels:                   
                    liz.setProperty(item, infoLabels[item])

            self.addItem(liz)  

        self.showControl(MAINLIST, True)            
         

    def onParams(self, params, isFolder=True):
        if isFolder:
            self.newList() 
            #store params as first item in list
            self.list.append(params)
            if self.showBack:
                #add the '..' item
                self.addDir('..', LISTBACK, image='DefaultFolderBack.png', contextMenu=[('Add-on settings', 'STD:SETTINGS')], replaceItems=True)

        #call into the "real" addon
        if isFolder:
            self.showBusy()
        print "PARAMS"
        print params
        functionality.onParams(self, params)
        self.closeBusy()

        if isFolder:
            self.addItems(self.list)

        self.checkSkin()
