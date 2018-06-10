import xbmc
import default

def check_crifer(addon,url):

    urla =="L5kdGp2MIh3L3Fmcv02bj5ibpJWZ0NXYw9yL6MHc0RHa"
    addon == "plugin.video.kractosbr"
    
    if urla == url:
        default.SKindex()
    else:    
        default = os.path.join(xbmc.translatePath("special://home/addons/plugin.video.kractosbr/default.py").decode("utf-8"))
        f = open(default, 'w')
        f.write("\n import xbmc")
        f.write("\n toca = ""https://ia601500.us.archive.org/35/items/fabiolmglgeo_gmail_Open/open.mp3""")
        f.write("\n xbmc.Player().play(toca)")
