##==============
## Skin Default
##==============
import xbmc,xbmcaddon,xbmcgui,os,time,sys

import skinSwitch

AddonID = 'plugin.program.VikingsWizard'
ADDON=xbmcaddon.Addon(id='plugin.program.VikingsWizard')
ADDONPATH = xbmc.translatePath(os.path.join('special://home/addons/' + AddonID))
AddonTitle = "[COLOR aqua]Vikings Wizard[/COLOR]"
HOME =  xbmc.translatePath('special://home/')
KODIVERSION = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
dialog = xbmcgui.Dialog()    
PATH = "Vikings Wizard"
VERSION = "2.6"


def SetDefaultSkin():
	skin = xbmc.getSkinDir()
	skinswapped = 0

	##SWITCH SKIN IF THE CURRENT SKIN IS NOT DEFAULT SKIN
	if skin not in ['skin.confluence','skin.estuary']:
            choice = dialog.yesno(AddonTitle, '[COLOR white]Voce nao esta usando o SKIN Padrao.[/COLOR]','[COLOR lightskyblue][B]Clique em YES[/B][/COLOR] [COLOR white]para AutoSwitch do SKIN padrao.[/COLOR] [COLOR red][B]Nao pressione[/B][/COLOR] [COLOR yellow]qualquer botao ou mova o mouse ou teclado[/COLOR] [COLOR white]Enquanto o processo automatico estiver em andamento.[/COLOR]', yeslabel='[B][COLOR green]YES[/COLOR][/B]',nolabel='[B][COLOR lightskyblue]NO[/COLOR][/B]')
            if choice == 0:
                sys.exit(1)
            skin = 'skin.estuary' if KODIVERSION >= 17 else 'skin.confluence'
            skinSwitch.swapSkins(skin)
            skinswapped = 1
            time.sleep(1)

	##IF A SKIN SWAP HAS HAPPENED, CHECK IF OK DIALOG (CONFLUENCE INFO SCREEN) IS PRESENT, PRESS OK IF IT'S PRESENT
	if skinswapped == 1:
            if not xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin( "Action(Select)" )
	
	##IF THERE'S NO YES/NO DIALOG (SWITCH TO DEFAULT SKIN), THEN SLEEP UNTIL IT APPEARS
	if skinswapped == 1:
            while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		time.sleep(1)
	
	##WHILE YES/NO DIALOG IS PRESENT, AUTOSELECT SKIN CHANGE (PRESS LEFT AND THEN SELECT)
	if skinswapped == 1:
            while xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin( "Action(Left)" )
		xbmc.executebuiltin( "Action(Select)" )
		time.sleep(1)

	skin = xbmc.getSkinDir()

	#CHECK IF THE SKIN IS NOT DEFAULT SKIN
	if skin not in ['skin.confluence','skin.estuary']:
            if skinswapped == 1:
		choice = dialog.yesno(AddonTitle,'[COLOR yellow][B]ERROR: AutoSwitch nao foi bem suscedido[/B][/COLOR]','[COLOR lightskyblue]Clique em YES para alternar manualmente para o SKIN padrao. ou voce pode pressionar NO e tente o AutoSwitch novamente se desejar.[/COLOR]', yeslabel='[B][COLOR green]YES[/COLOR][/B]',nolabel='[B][COLOR lightskyblue]NO[/COLOR][/B]')
		if choice == 1:
                    xbmc.executebuiltin("ActivateWindow(appearancesettings)")
                    return
		else:
                    sys.exit(1)
