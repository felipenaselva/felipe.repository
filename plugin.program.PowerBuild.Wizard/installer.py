##==============
## Installer
##===============
import xbmc,xbmcaddon,xbmcgui,os,time
import skindefault
import downloader
import extract
import common

AddonID = 'plugin.program.PowerBuild.Wizard'
ADDON=xbmcaddon.Addon(id='plugin.program.PowerBuild.Wizard')
HOME =  xbmc.translatePath('special://home/')   
PATH = "PowerBuild Wizard"
VERSION = "2.6"

##============
##   WIZARD
##============
def WIZARD(name,url,description):
    AddonTitle = "[COLOR aqua]PowerBuild Wizard[/COLOR]"
    KODIVERSION = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
    dialog = xbmcgui.Dialog()
    if KODIVERSION < 16.0:
        dialog.ok("[COLOR=red][B]Atencao !!! [/COLOR][/B]", "Seu dispositivo possui uma versao antiga do Kodi que deve ser atualizada.")
        return
    else:
        skindefault.SetDefaultSkin()
        dp = xbmcgui.DialogProgress()

        ##  Fresh Start
        dp.create(AddonTitle,"Restaurando Kodi.",'Em progresso.............','Por favor aguarde...')
        common.FRESHSTARTBUILD()
        time.sleep(2)

        ##  Download
        dp.create(AddonTitle,"Carregando a ultima compilacao... ",'','Por favor aguarde...')
        path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
        lib=os.path.join(path, name+'.zip')
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib, dp)
        time.sleep(2)

        ##  Extract from Zip File
        addonfolder = xbmc.translatePath(os.path.join('special://','home'))
        dp.update(0,"", "Extraindo arquivos do ZIP...")
        extract.all(lib,addonfolder,dp)

        ##  Cleanup Kodi
        common.CLEANUP(url)
        time.sleep(2)

        ##  Force Quit Kodi
        common.TIMER(15,"[COLOR aqua][B]O DOWNLOAD esta completo[/B][/COLOR]","O Kodi desligara automaticamente em: ", "Para dispositivo Android/Amazon: [COLOR yellow][B]Remova o cabo de energia[/B][/COLOR] do seu dispositivo [COLOR red][B]APOS[/B][/COLOR] a contagem regressiva.")
        common.killxbmc()
