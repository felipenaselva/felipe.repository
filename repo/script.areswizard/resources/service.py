import xbmc

try:
	xbmc.executebuiltin("RunPlugin(plugin://script.areswizard/?start='checkbuild')", True)
except:
	pass