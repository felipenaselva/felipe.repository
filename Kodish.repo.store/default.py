# -*- coding: cp1252 -*-
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys
import shutil
import urllib2,urllib
import re
import extract
import time
import downloader
import plugintools
import zipfile
import ntpath
import ssl
import traceback,sys
from libs import kodi
from libs import viewsetter
import checksun

icon = os.path.join(xbmc.translatePath("special://home/addons/Kodish.repo.store/icon.png").decode("utf-8"))

if kodi.get_kversion() >16.5:
	#kodi.log(' VERSION IS ABOVE 16.5')
	ssl._create_default_https_context = ssl._create_unverified_context
else:
	#kodi.log(' VERSION IS BELOW 16.5')
	pass
from libs import addon_able


USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
base='http://kodish.esy.es'
ADDON=xbmcaddon.Addon(id='Kodish.repo.store')
    
    
VERSION = "1.0.2"
PATH = "kodish.esy.es"            


def CATEGORIES():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/kodishchester').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def KRATOSVIP():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/kratosvip').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def CATEGORIES2():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/kodishstoreraptor2').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def Reposkodish():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/repos-kodishstore').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def RESTRITOM18():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/so18').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')


def TVADDONS():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/tvaadons').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def ATIVAR():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/ative').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')


def PREMIUM():
    link = OPEN_URL('https://raw.githubusercontent.com/kodishmediacenter/store/master/premiun').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')
	
def Lojink():
    link = OPEN_URL('https://pastebin.com/raw/sPH6k4h7').replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,1,iconimage,fanart,description)
    setView('movies', 'MAIN')

def EXTSETUP():
        keylink = xbmc.Keyboard('', 'Digite Um Friendly Link:')
        keylink.doModal()
        ulink = keylink.getText()
        link = OPEN_URL(""+ulink+"").replace('\n','').replace('\r','')
        match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
        for name,url,iconimage,fanart,description in match:
            addDir(name,url,1,iconimage,fanart,description)
        setView('movies', 'MAIN')

def EXTZSETUP():
        keylink = xbmc.Keyboard('', 'Cole o arquivo zip de um addon ou Repositorio:')
        keylink.doModal()
        ulink = keylink.getText()
        link = OPEN_URL("https://raw.githubusercontent.com/kodishmediacenter/store/master/zip").replace('\n','').replace('\r','')
        match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
        name = "Zip Instaler"
        #url  = ""+ulink+""
        iconimage = ""
        description = "[COLOR Yellow]Zip Instaler[/COLOR]"
        for name,url,iconimage,fanart,description in match:
            url  = ""+ulink+""
            addDir(name,url,1,iconimage,fanart,description)
            setView('movies', 'MAIN')

# mexus instruction

def mexus_kernel():
        mexus = xbmc.Keyboard('', '1 Visualizar Log do Kodi:')
        mexus.doModal()
        chavemexus = mexus.getText()
        
        if chavemexus == "1":
                logr = os.path.join(xbmc.translatePath("special://home/addons/webinterface.kratos/log.html").decode("utf-8"))
                logrr = os.path.join(xbmc.translatePath("special://logpath/kodi.log").decode("utf-8"))
                arq = open(logrr, 'r')
                arq2 = open(logr, 'w')
                texto = arq.readlines()
                arq2.write("<PRE>")
                for linha in texto :
                    arq2.write(linha)
                arq2.write("</PRE>")
                arq.close()
                arq2.close()

        
                
        
    

def SETUP_REPO():
        
        xbmc.executebuiltin("ActivateWindow(10040,&quot;addons://install/&quot;,return)")

def SETUP_ADDONS():
        
        xbmc.executebuiltin("ActivateWindow(addons://sources/video/addons)")


def login():
        dialog = xbmcgui.Dialog()
        d = dialog.input('[COLOR yellow]Digite 0 Padrao 13 Lojink 10 Instalacao Manual 11 Ativar addons :[/COLOR]', type=xbmcgui.INPUT_ALPHANUM)
        key = int(""+d+"")
        
        if key == 660655:
            #T
            RESTRITOM18()
            #CATEGORIES()
       
        if key == 10:
            #TVADDONS()
            SETUP_REPO()

        if key ==11:
            ATIVAR()

        if key == 102347:
            PREMIUM()
             
        if key == 102348:
            CATEGORIES()
            
        if key == 0:
            CATEGORIES2()
            CATEGORIES()
			
	if key == 12:
	    Lojink()
            TVADDONS()
            CATEGORIES2()
            CATEGORIES()		
            RESTRITOM18()
            
        if key == 13:
            Lojink()
            
        if key == 1:
            EXTSETUP()

        if key == 2:
            EXTZSETUP()
            
        if key == 999:
            time.sleep(2)
            killxbmc()

        if key == 2562124:
            KRATOSVIP()

        if key == 999999:
            mexus_kernel()

        if key == 999998:
            menukodish()


        
def loginmx(op):
        key = op
        
        if key == 660655:
            #T
            RESTRITOM18()
            #CATEGORIES()
       
        if key == 10:
            #TVADDONS()
            SETUP_REPO()

        if key ==11:
            ATIVAR()

        if key == 102347:
            PREMIUM()
             
        if key == 102348:
            CATEGORIES()
            
        if key == 0:
            CATEGORIES2()
            CATEGORIES()
			
	if key == 12:
	    Lojink()
            TVADDONS()
            CATEGORIES2()
            CATEGORIES()		
            RESTRITOM18()
            
        if key == 13:
            Lojink()
            
        if key == 1:
            EXTSETUP()

        if key == 2:
            EXTZSETUP()
            
        if key == 999:
            time.sleep(2)
            killxbmc()

        if key == 2562124:
            KRATOSVIP()

        if key == 999999:
            mexus_kernel()

        if key == 999998:
            menukodish()
        

def setup_op():
       dialog = xbmcgui.Dialog()
       link = dialog.select('Bem Vindo Area Homebrew', ['Friend Link', 'Instalação via Link (Tem saber as dependencias)'])

       if link == 0:
            EXTSETUP()
       if link == 1:
            EXTZSETUP()
        
def menukodish():
       dialog = xbmcgui.Dialog()
       ret = dialog.select('[COLOR yellow]Bem Vindo a Kodish Store[/COLOR]', ['Addons Gerais', 'Kodi Repositorios','Lojink', 'Ativar Addon (kodi17)','Ativar Addon Manualmente (kodi17)','Addons Nao Homologados Homebrew','Salvar o Log do Kodi'])

       if ret == 0:
            CATEGORIES2()
            CATEGORIES()
       if ret == 1:
            Reposkodish()
       if ret == 2:
            Lojink()
            
       if ret == 3:
            ATIVAR()

       if ret == 4:
            SETUP_REPO()

       if ret == 5: 
           setup_op()
           
       if ret == 6:
           mexus_kernel()
           
               

        
        
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    
    
def wizard(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("Addon Selecionado","Baixando ",'', 'Por Favor Espere')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home/','addons'))
    time.sleep(2)
    dp.update(0,"", "Instalando Por Favor Espere")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    #dialog = xbmcgui.Dialog()
    #dialog.ok("Baixado com Sucesso:)", 'Para continuar a Instalacao irar ser solicitado que desligue o Kodi', 'Se for uma Box precione [COLOR yellow]NAO[/COLOR] depois sai do kodi para terminar a instalacao.','[COLOR yellow][B][Kodi 17][/B][/COLOR]Ao Voltar vai Addons em Meus Addons ativa o addons instalado')
    time.sleep(2)
    xbmc.executebuiltin("XBMC.UpdateLocalAddons()");
    addon_able.set_enabled("")
    addon_able.setall_enable()
    #killxbmc()
        
      
        
def killxbmc():
    choice = xbmcgui.Dialog().yesno('Desligando o Kodi', 'Desligando o Kodi ou SPMC', 'Vc quer continuar ?', nolabel='Nao, irei instalar Mais Addons ou Android Box',yeslabel='Sim, Vou Sair')
    if choice == 0:
        return
    elif choice == 1:
        pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=blue]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=blue]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'android': # Android  
        print "############   try android force close  #################"
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass        
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "Your system has been detected as Android, you ", "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=blue]DO NOT[/COLOR] exit cleanly via the menu.","Pulling the power cable is the simplest method to force close.")
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
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
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im SPMC.exe /f')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=blue]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=blue]DO NOT[/COLOR] exit via the menu.","Your platform could not be detected so just pull the power cable.")    

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


def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
       
        
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
        
                      
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
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
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
        
        
if mode==None or url==None or len(url)<1:
        checksun.checkrato()
        menukodish()
        
       
elif mode==1:
        
        wizard(name,url,description)

elif mode==101:
        TVADDONS()
        CATEGORIES()
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

        
xbmcplugin.endOfDirectory(int(sys.argv[1]))

