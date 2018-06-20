##===========================
## Vikings Wizard - Common
##===========================
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys,urllib,urllib2
from urllib2 import urlopen
import plugintools

AddonID = 'plugin.program.VikingsWizard'
ADDON=xbmcaddon.Addon(id='plugin.program.VikingsWizard')
ADDONPATH = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID))
HOME =  xbmc.translatePath('special://home/')
dialog = xbmcgui.Dialog()    
PATH = "Vikings Wizard"


##=======================
##   FRESH START KODI 
##=======================
def FRESHSTARTBUILD():
    addonPath=xbmcaddon.Addon(id=AddonID).getAddonInfo('path')
    addonPath=xbmc.translatePath(addonPath) 
    xbmcPath=os.path.join(addonPath,"..","..")
    xbmcPath=os.path.abspath(xbmcPath)
    plugintools.log("freshstart.main_list xbmcPath="+xbmcPath)
    failed=False
    ## Real Debrid and Trakt Files
    ADDON_DATA=xbmc.translatePath(os.path.join('special://home/userdata','addon_data'))
    Trakt_AD=xbmc.translatePath(os.path.join(ADDON_DATA,'script.trakt'))
    URL_Resolver_AD=xbmc.translatePath(os.path.join(ADDON_DATA,'script.module.urlresolver'))
    Specto_AD=xbmc.translatePath(os.path.join(ADDON_DATA,'plugin.video.specto'))
    ## Excluded Directories
    EXCLUDES1 = ['plugin.program.VikingsWizard','script.module.addon.common','packages',Trakt_AD,URL_Resolver_AD,Specto_AD]                      
    ## Excluded Files
    EXCLUDES2 = ['favourites.xml','advancedsettings.xml','profiles.xml']
    
    for root, dirs, files in os.walk(xbmcPath,topdown=True):
        dirs[:] = [d for d in dirs if d not in EXCLUDES1]
        for name in files:
            if name not in EXCLUDES2:
                try: os.remove(os.path.join(root,name))
                except:
                    if name not in ["Addons15.db","MyVideos75.db","Textures13.db","xbmc.log"]: failed=True
                    plugintools.log("Error removing "+root+" "+name)

        for name in dirs:
            try: os.rmdir(os.path.join(root,name))
            except:
                if name not in ["Database","userdata"]: failed=True
                plugintools.log("Error removing "+root+" "+name)
        else:
            pass

##===========================
##  Clear Cache & Packages
##===========================
def CLEANUP(url):
    print '############################################################       DELETING PACKAGES             ###############################################################'
    packages_cache_path = xbmc.translatePath(os.path.join('special://home/addons/packages', ''))
    try:    
        for root, dirs, files in os.walk(packages_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
    except:
        ADDONTITLE = "[COLOR aqua]Vikings [/COLOR] [COLOR white]Wizard[/COLOR]" 
        dialog = xbmcgui.Dialog()
        dialog.ok(ADDONTITLE, "Desculpe, nao conseguimos remover arquivos de pacote", "")
	print '############################################################       DELETING STANDARD CACHE             ###############################################################'
    xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'), 'cache')
    if os.path.exists(xbmc_cache_path)==True:    
        for root, dirs, files in os.walk(xbmc_cache_path):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                for f in files:
                    try:
                        os.unlink(os.path.join(root, f))
                    except:
                        pass
                for d in dirs:
                    try:
                        hutil.rmtree(os.path.join(root, d))
                    except:
                        pass        
            else:
                pass

##============
##   Timer
##============
def TIMER(timer,title,text,text2):
    box = xbmcgui.DialogProgress()
    ret = box.create(' '+title)
    secs=0
    percent=0
    increment = int(100 / timer)
    while secs < timer:
        secs += 1
        percent = increment*secs
        secs_left = str((timer - secs))
        remaining_display = '[COLOR red][B]' + str(secs_left) + " segundos" + '[/B][/COLOR]'
        box.update(percent,text + remaining_display,"", text2)
        xbmc.sleep(1000)

##=================
##  Add to menus
#==================
def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok


def addItem(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty( "Fanart_Image", fanart )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addDirWTW(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name, url, mode, iconimage):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode)\
        + "&name=" + urllib.quote_plus(name)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png",
                           thumbnailImage=iconimage)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u,
                                     listitem=liz, isFolder=False)
    return ok


##=====================
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

##=======================
##  DETERMINE PLATFORM
##=======================
def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

##===============================
## FORCE CLOSE KODI
## ANDROID ONLY WORKS IF ROOTED
##===============================
def killxbmc():
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx':
        print "############   try MacOS Force Close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR=red][B]Atencao  !!![/COLOR][/B]","Se voce esta vendo esta mensagem, significa que o Auto Force Close nao teve exito. [COLOR yellow][B]Por favor force o fechamento do KODI.[/B][/COLOR] [COLOR=lime]Nao[/COLOR] saia do Kodi pelo Menu.")
    elif myplatform == 'linux':
        print "############   try Linux Force Close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR=red][B]Atencao  !!![/COLOR][/B]","Se voce esta vendo esta mensagem, significa que o Auto Force Close nao teve exito. [COLOR yellow][B]Por favor force o fechamento do KODI.[/B][/COLOR] [COLOR=lime]Nao[/COLOR] saia do Kodi pelo Menu.")
    elif myplatform == 'android':
        print "############   try Android Force Close  #################"
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass                
        dialog.ok("[COLOR=red][B]Atencao  !!![/COLOR][/B]", "Se voce esta vendo esta mensagem, significa que o Auto Force Close nao teve exito. [COLOR=lime]Nao[/COLOR] saia do Kodi pelo Menu. Ao inves disto [COLOR yellow][B]Remova o cabo de energia[/B][/COLOR] do seu dispositivo, aguarde 15 Segundos, Reconecte o cabo de energia, e entre no Kodi.")
    elif myplatform == 'windows':
        print "############   try Windows Force Close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog.ok("[COLOR=red][B]Atencao  !!![/COLOR][/B]", "Se voce esta vendo esta mensagem, significa que o Auto Force Close nao teve exito. [COLOR yellow][B]Por favor force o fechamento do KODI.[/B][/COLOR] [COLOR=lime]Nao[/COLOR] saia do Kodi pelo Menu. Em vez disso use o Gerenciador de Tarefas, mas nao ALT-F4")
    elif myplatform == 'ios':
        ## No Force Close for iOS Devices
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "Se voce esta vendo esta mensagem, significa que o Auto Force Close nao teve exito. [COLOR yellow][B]Por favor force o fechamento do KODI[/B][/COLOR] from the App Switcher. [COLOR=lime]DO NOT[/COLOR] exit from the KODI exit menu.")
    else:
        print "############   try Apple TV Force Close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try Raspbmc Force Close  #################"
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]Atencao  !!![/COLOR][/B]", "e voce esta vendo esta mensagem, significa que o Auto Force Close nao teve exito. [COLOR yellow][B]Por favor force o fechamento do KODI.[/B][/COLOR] [COLOR=lime]Nao[/COLOR] saia do Kodi pelo Menu. seu dispositivo e desconhecido, entao, remova o cabo de alimentacao, aguarde 15 segundos e reconecte o cabo novamente.")   

