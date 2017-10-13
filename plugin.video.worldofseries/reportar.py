import subprocess
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmc

def report():
    osWin = xbmc.getCondVisibility('system.platform.windows')
    osOsx = xbmc.getCondVisibility('system.platform.osx')
    osLinux = xbmc.getCondVisibility('system.platform.linux')
    osAndroid = xbmc.getCondVisibility('system.platform.linux')

    if osWin:
         subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe","https://form.jotformz.com/72838708513665"])
    if  osAndroid:
        cmd = 'StartAndroidActivity(com.android.chrome,android.intent.action.VIEW,,https://form.jotformz.com/72838708513665)'
        xbmc.executebuiltin(cmd)
    if  osLinux:
       subprocess.call(["/usr/bin/google-chrome","https://form.jotformz.com/72838708513665"])
    if osOsx:
        r = subprocess.call(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome","https://form.jotformz.com/72838708513665"])
       

