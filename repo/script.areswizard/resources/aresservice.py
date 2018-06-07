import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , sys
import urllib2 , urllib , re , base64
import shutil , glob , json , os . path
import time
from xbmc import translatePath as translate
#import imp
import datetime
import zipfile
import xml . etree . ElementTree as ET
from xml . etree . ElementTree import Element
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii






def writelog(message, level=xbmc.LOGNOTICE):
	"""
	Write a debug message to xbmc.log

	:type message: str
	:param message: the message to log
	:type level: int
	:param level: (Optional) the log level (supported values are found at xbmc.LOG...)
	"""
	if isinstance(message, unicode):
		message = message.encode("utf-8")
	for line in message.splitlines():
		xbmc.log(msg='Ares Wizard - Service' + ": " + line, level=level)
		
		

	
		
		
	# areslog = os.path.join(datapath, timestr2)
		
	# with open(areslog, 'a') as f:
		

		# f.write(message + "\n")
		# f.close







IiII1IiiIiI1 = translate ( 'special://home/addons/script.areswizard' )
iIiiiI1IiI1I1 = translate ( 'special://home/addons' )
o0OoOoOO00 = translate ( 'special://home/userdata/addon_data/script.areswizard' )
I11i = os . path . join ( IiII1IiiIiI1 , 'icon.png' )
O0O = os . path . join ( o0OoOoOO00 , 'settings' )
Oo = os . path . join ( o0OoOoOO00 , 'settings.xml' )
I1ii11iIi11i = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
I1IiI = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'temp' )
o0OOO = os . path . join ( xbmc . translatePath ( IiII1IiiIiI1 ) , 'default.py' )
iIiiiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
Iii1ii1II11i = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Thumbnails' , '' ) )
iI111iI = translate ( 'special://home/addons/script.areswizard/resources/images' )
IiII = os . path . join ( iI111iI , 'button_default.png' )
iI1Ii11111iIi = os . path . join ( iI111iI , 'button_selected.png' )
i1i1II = os . path . join ( o0OoOoOO00 , 'buildinstall' )
O0oo0OO0 = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
if 6 - 6: oooO0oo0oOOOO - ooO0oo0oO0 - i111I * II1Ii1iI1i
if 12 - 12: o0oOoO00o
i1 = "none"
oOOoo00O0O = "no"
i1111 = "no"
i11 = "no"
if 41 - 41: O00o0o0000o0o . oOo0oooo00o * I1i1i1ii - IIIII
global I1
if 54 - 54: oO % IiiIIiiI11 / oooOOOOO * IiiIII111ii / i1iIIi1
if 50 - 50: i11iIiiIii - oO
if 78 - 78: i111I
Iii1I111 = 0
while Iii1I111 < 1000 :
 try :
  datetime . datetime . strptime ( '20110101' , '%Y%m%d' )
  Iii1I111 = 2001
 except :
  xbmc . sleep ( 1 )
  Iii1I111 += 1
  if 60 - 60: oOo0oooo00o * o0oOoO00o % o0oOoO00o % IIIII * II111iiii + i1IIi
if Iii1I111 != 2001 :
 datetime . datetime . strptime ( '20110101' , '%Y%m%d' )
 if 64 - 64: oOo0oooo00o - O0 / II111iiii / o0oOoO00o / iIii1I11I1II1
 if 24 - 24: O0 % o0oOoO00o + i1IIi + IiiIII111ii + O00o0o0000o0o
OOoO000O0OO = chr
def iiI1IiI ( i1Ii11i11 ) :
 if i1Ii11i11 :
  return OOoO000O0OO ( i1Ii11i11 % 256 ) + iiI1IiI ( i1Ii11i11 // 256 )
 else :
  return ""
  if 13 - 13: ooO0oo0oO0 . i11iIiiIii - iIii1I11I1II1 - II1Ii1iI1i
  if 6 - 6: oooO0oo0oOOOO / ooO0oo0oO0 % oO
def oo ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : OO0O00 = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : OO0O00 = ''
 else :
  try : OO0O00 = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : OO0O00 = ''
 return OO0O00
 if 20 - 20: OoooooooOO
 if 13 - 13: i1IIi - oO % oOo0oooo00o / iIii1I11I1II1 % IiiIIiiI11
 if 97 - 97: i11iIiiIii
 if 32 - 32: ooO0oo0oO0 * O0 % oOo0oooo00o % oO . oooOOOOO
 if 61 - 61: i1iIIi1
 if 79 - 79: ooO0oo0oO0 + oooO0oo0oOOOO - IiiIIiiI11
def oO00O00o0OOO0 ( path , showerror ) :
 if 27 - 27: O0 % i1IIi * oOo0oooo00o + i11iIiiIii + OoooooooOO * i1IIi
 path = path . encode ( 'utf-8' )
 if 80 - 80: IIIII * i11iIiiIii / IiiIII111ii
 if 9 - 9: oO + oOo0oooo00o % oO + i1IIi . I1i1i1ii
 if serverhttp in path :
  if 31 - 31: o0oOoO00o + IIIII + IIIII / II111iiii
  path = path . replace ( serverhttp , serverhttps )
  if 26 - 26: OoooooooOO
  if 12 - 12: OoooooooOO % II1Ii1iI1i / i1iIIi1 % o0oOoO00o
 xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 if 29 - 29: OoooooooOO
 iI = urllib2 . Request ( path )
 iI . add_header ( 'User-Agent' , I1i1I1II )
 if 45 - 45: IiiIII111ii . II1Ii1iI1i
 if 83 - 83: oOo0oooo00o . iIii1I11I1II1 . O00o0o0000o0o
 if 31 - 31: oO . oO - o0oOoO00o / i111I + i1iIIi1 * oooO0oo0oOOOO
 if 63 - 63: IiiIII111ii % i1IIi / OoooooooOO - OoooooooOO
 if 8 - 8: II1Ii1iI1i
 try :
  o00O = urllib2 . urlopen ( iI )
  if 69 - 69: oOo0oooo00o % IiiIII111ii - o0oOoO00o + IiiIII111ii - O0 % OoooooooOO
 except HTTPError , Iii111II :
  if 9 - 9: i111I
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  error = Iii111II . code
  error = error . encode ( 'utf-8' )
  if showerror == "Yes" :
   i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
   i11O0oo0OO0oOOOo . ok ( "HTTP Error" , str ( error ) , "" , "" )
  writelog('@Ares: HTTP Error: ' + str ( error ))
  if debuglog == "true" :
   writelog(path)
  return ( 'downloadfailed' )
  if 35 - 35: oooOOOOO % oooO0oo0oOOOO
 except URLError , Iii111II :
  if 70 - 70: IiiIIiiI11 * O00o0o0000o0o
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  error = Iii111II . reason
  error = error . encode ( 'utf-8' )
  if showerror == "Yes" :
   i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
   i11O0oo0OO0oOOOo . ok ( "URL Error" , str ( error ) , "" , "" )
  writelog('@Ares: URL Error: ' + str ( error ))
  if debuglog == "true" :
   writelog(path)
  return ( 'downloadfailed' )
 except IOError , Iii111II :
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  error = Iii111II . errno
  error = error . encode ( 'utf-8' )
  error2 = Iii111II . strerror
  error2 = error2 . encode ( 'utf-8' )
  if showerror == "Yes" :
   i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
   i11O0oo0OO0oOOOo . ok ( "IO Error" , str ( error ) + " - " + str ( error2 ) , "" , "" )
  writelog('@Ares: IO Error: ' + str ( error ) + ' - ' + str ( error2 ))
  if debuglog == "true" :
   writelog(path)
  return ( 'downloadfailed' )
 except ssl . SSLError , Iii111II :
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  error = Iii111II . reason
  error = error . encode ( 'utf-8' )
  writelog('@Ares: SSL Error: ' + str ( error ))
  if showerror == "Yes" :
   i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
   i11O0oo0OO0oOOOo . ok ( "Ares Wizard" , "Failed to reach Ares server (SSL Error) this could be due to security restrictions on your network." )
  if debuglog == "true" :
   writelog(path)
  return ( 'downloadfailed' )
  if 46 - 46: i1iIIi1 / i111I
 except Exception , Iii111II :
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  error = Iii111II . reason
  error = error . encode ( 'utf-8' )
  if error == "" :
   error = "Unknown Exception"
  if showerror == "Yes" :
   i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
   i11O0oo0OO0oOOOo . ok ( "Unknown Error" , str ( error ) , "" , "" )
  writelog('@Ares: Unknown Error: ' + str ( error ))
  if debuglog == "true" :
   writelog(path)
  return ( 'downloadfailed' )
  if 52 - 52: o0oOoO00o - OoooooooOO + oO + oO - o0oOoO00o / IiiIII111ii
 except :
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if showerror == "Yes" :
   i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
   i11O0oo0OO0oOOOo . ok ( "Unknown Error" , "Unspecified Error (sorry)" , "" , "" )
  writelog('@Ares: Unknown Error: Unspecified')
  if debuglog == "true" :
   writelog(path)
  return ( 'downloadfailed' )
  if 44 - 44: i1iIIi1 . i1IIi - O00o0o0000o0o . O0 - i1iIIi1
  if 92 - 92: IiiIIiiI11 . IIIII + o0oOoO00o
 try :
  IiII1I11i1I1I = o00O . read ( )
  if 83 - 83: O00o0o0000o0o / i1iIIi1
 except socket . timeout :
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if showerror == "Yes" :
   i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
   i11O0oo0OO0oOOOo . ok ( "Socket Error" , "Socket Timeout" , "" , "" )
  writelog('@Ares: Socket Error: Socket Timeout')
  if debuglog == "true" :
   writelog(path)
  return ( 'downloadfailed' )
  if 49 - 49: o0oOoO00o
  if 35 - 35: II1Ii1iI1i - OoooooooOO / O00o0o0000o0o % i1IIi
 except socket . error :
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if showerror == "Yes" :
   i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
   i11O0oo0OO0oOOOo . ok ( "Socket Error" , "Socket Error" , "" , "" )
  writelog('@Ares: Socket Error: Socket Error')
  if debuglog == "true" :
   writelog(path)
  return ( 'downloadfailed' )
  if 78 - 78: IIIII
 xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
 if 71 - 71: I1i1i1ii + i1iIIi1 % i11iIiiIii + O00o0o0000o0o - oooOOOOO
 return ( IiII1I11i1I1I )
 if 88 - 88: II1Ii1iI1i - i111I % I1i1i1ii
 if 16 - 16: oooO0oo0oOOOO * oOo0oooo00o % oooOOOOO
 if 86 - 86: oooO0oo0oOOOO + oO % i11iIiiIii * oOo0oooo00o . i1iIIi1 * IIIII
 if 44 - 44: oOo0oooo00o
def o0o0oOoOO0 ( start_path ) :
 if 17 - 17: oooOOOOO
 global total_files
 global total_size
 if 62 - 62: iIii1I11I1II1 * II1Ii1iI1i
 if 26 - 26: IiiIIiiI11 . IiiIII111ii
 total_size = 0
 total_files = 0
 for oOOOOo0 , iiII1i1 , o00oOO0o in os . walk ( start_path ) :
  for OOO00O in o00oOO0o :
   OOoOO0oo0ooO = os . path . join ( oOOOOo0 , OOO00O )
   total_size += os . path . getsize ( OOoOO0oo0ooO )
   total_files = total_files + 1
 return total_size
 if 98 - 98: IiiIIiiI11 * IiiIIiiI11 / IiiIIiiI11 + IIIII
 if 34 - 34: i1iIIi1
def I1111I1iII11 ( ) :
 if 59 - 59: iIii1I11I1II1 * i11iIiiIii / O00o0o0000o0o * i1IIi * O0
 global tempandcachefiles
 global tempandcachesize
 if 83 - 83: i111I / IiiIII111ii . II1Ii1iI1i / oooOOOOO . II1Ii1iI1i . I1i1i1ii
 tempandcachefiles = 0
 tempandcachesize = 0
 if 75 - 75: IIIII + i111I . II1Ii1iI1i . i1iIIi1 + ooO0oo0oO0 . i111I
 o0o0oOoOO0 ( I1IiI )
 tempandcachefiles = tempandcachefiles + total_files
 tempandcachesize = tempandcachesize + ( total_size / 1024 / 1024 )
 if 96 - 96: I1i1i1ii . i1iIIi1 - ooO0oo0oO0 + iIii1I11I1II1 / II1Ii1iI1i * I1i1i1ii
 o0o0oOoOO0 ( I1ii11iIi11i )
 tempandcachefiles = tempandcachefiles + total_files
 tempandcachesize = tempandcachesize + ( total_size / 1024 / 1024 )
 if 65 - 65: oO . iIii1I11I1II1 / O0 - oO
 if 21 - 21: oooO0oo0oOOOO * iIii1I11I1II1
 if 91 - 91: oooOOOOO
def iiIii ( settingid , value ) :
 if 79 - 79: OoooooooOO / O0
 try :
  if 75 - 75: II1Ii1iI1i % o0oOoO00o % o0oOoO00o . IiiIII111ii
  if 5 - 5: o0oOoO00o * i1iIIi1 + II1Ii1iI1i . I1i1i1ii + II1Ii1iI1i
  with open ( O0O , 'r' , 0 ) as OOO00O :
   oOiIi1IIIi1 = json . load ( OOO00O )
   if 86 - 86: IIIII % II1Ii1iI1i / oooO0oo0oOOOO / II1Ii1iI1i
  iIIi1i1 = oOiIi1IIIi1 [ 'deviceid' ]
  if 10 - 10: IIIII
  if 82 - 82: O00o0o0000o0o - iIii1I11I1II1 / I1i1i1ii + oO
  if 87 - 87: oOo0oooo00o * O00o0o0000o0o + I1i1i1ii / iIii1I11I1II1 / IiiIIiiI11
  try :
   I1111IIi = oOiIi1IIIi1 [ 'automaintenance' ]
  except :
   I1111IIi = "0"
   if 93 - 93: OoooooooOO / oooO0oo0oOOOO % i11iIiiIii + O00o0o0000o0o * i111I
   if 15 - 15: IIIII . i111I / ooO0oo0oO0 + IIIII
  try :
   Ooo = oOiIi1IIIi1 [ 'storageinfolastpopup' ]
  except :
   Ooo = "0"
   if 62 - 62: I1i1i1ii / i111I + oO / i111I . II111iiii
   if 68 - 68: i11iIiiIii % O00o0o0000o0o + i11iIiiIii
  try :
   iii = oOiIi1IIIi1 [ 'fullautofreq' ]
  except :
   iii = "0"
   if 1 - 1: ooO0oo0oO0 / o0oOoO00o % IiiIIiiI11 * oooOOOOO . i11iIiiIii
   if 2 - 2: O00o0o0000o0o * IIIII - iIii1I11I1II1 + oooO0oo0oOOOO . oOo0oooo00o % IiiIIiiI11
  try :
   ooOOOoOooOoO = oOiIi1IIIi1 [ 'fullautocache' ]
  except :
   ooOOOoOooOoO = "0"
   if 91 - 91: IiiIIiiI11 % i1IIi % iIii1I11I1II1
   if 20 - 20: I1i1i1ii % oO / oO + oO
  try :
   III1IiiI = oOiIi1IIIi1 [ 'fullautopackages' ]
  except :
   III1IiiI = "0"
   if 31 - 31: o0oOoO00o . oooO0oo0oOOOO
   if 46 - 46: IiiIIiiI11
  try :
   IIIII11I1IiI = oOiIi1IIIi1 [ 'fullautothumb' ]
  except :
   IIIII11I1IiI = "0"
   if 16 - 16: iIii1I11I1II1
   if 90 - 90: o0oOoO00o % i1IIi / i111I
   if 44 - 44: ooO0oo0oO0 . i111I / O00o0o0000o0o + oO
   if 65 - 65: O0
   if 68 - 68: I1i1i1ii % IiiIII111ii
  try :
   ooO00OO0 = oOiIi1IIIi1 [ 'cacheinclude_genesis' ]
  except :
   ooO00OO0 = "0"
   if 31 - 31: IiiIIiiI11 % IiiIIiiI11 % IIIII
  try :
   OOOOoo0Oo = oOiIi1IIIi1 [ 'cacheinclude_navix' ]
  except :
   OOOOoo0Oo = "0"
   if 14 - 14: IiiIIiiI11
  try :
   I1iI1iIi111i = oOiIi1IIIi1 [ 'cacheinclude_youtube' ]
  except :
   I1iI1iIi111i = "0"
   if 44 - 44: i1IIi % II111iiii + IIIII
  try :
   I1I1I = oOiIi1IIIi1 [ 'cacheinclude_ivue' ]
  except :
   I1I1I = "0"
   if 95 - 95: II111iiii + o0oOoO00o + IiiIIiiI11 * iIii1I11I1II1 % oOo0oooo00o / oooOOOOO
  try :
   o0o0o0oO0oOO = oOiIi1IIIi1 [ 'cacheinclude_salts' ]
  except :
   o0o0o0oO0oOO = "0"
   if 3 - 3: o0oOoO00o
  try :
   Ii11I1 = oOiIi1IIIi1 [ 'cacheinclude_pulsar' ]
  except :
   Ii11I1 = "0"
   if 14 - 14: I1i1i1ii % iIii1I11I1II1
   if 71 - 71: O0 . IiiIIiiI11 / o0oOoO00o
   if 73 - 73: II111iiii . i11iIiiIii / oO + II1Ii1iI1i
   if 12 - 12: i11iIiiIii - i1IIi - i111I . i1IIi - I1i1i1ii + O0
  try :
   oO0OOOO0 = oOiIi1IIIi1 [ 'totaltempfiles' ]
  except :
   oO0OOOO0 = "0"
   if 26 - 26: oO
  try :
   I11iiI1i1 = oOiIi1IIIi1 [ 'totalspacegained' ]
  except :
   I11iiI1i1 = "0"
   if 47 - 47: IiiIIiiI11 - oO . II111iiii + OoooooooOO . i11iIiiIii
   if 94 - 94: o0oOoO00o * oO / ooO0oo0oO0 / oO
  try :
   oO0 = oOiIi1IIIi1 [ 'lastbuildcheck' ]
  except :
   oO0 = "0"
   if 75 - 75: i1iIIi1 + II1Ii1iI1i + o0oOoO00o * IIIII % oOo0oooo00o . IiiIIiiI11
   if 55 - 55: I1i1i1ii . oooO0oo0oOOOO
  try :
   oOo0O0o00o = oOiIi1IIIi1 [ 'buildupdate' ]
  except :
   oOo0O0o00o = "0"
   if 64 - 64: I1i1i1ii % iIii1I11I1II1 * oOo0oooo00o
   if 79 - 79: O0
   if 78 - 78: O00o0o0000o0o + I1i1i1ii - IiiIII111ii
   if 38 - 38: o0oOoO00o - oOo0oooo00o + iIii1I11I1II1 / II1Ii1iI1i % ooO0oo0oO0
  if settingid == "storageinfolastpopup" :
   Ooo = value
   if 57 - 57: i111I / i1iIIi1
   if 29 - 29: iIii1I11I1II1 + II1Ii1iI1i * i111I * I1i1i1ii . oooO0oo0oOOOO * oooO0oo0oOOOO
  if settingid == "lastbuildcheck" :
   oO0 = value
   if 7 - 7: oooOOOOO * IiiIII111ii % oO - o0oOoO00o
   if 13 - 13: oO . i11iIiiIii
  if settingid == "buildupdate" :
   oOo0O0o00o = value
   if 56 - 56: O00o0o0000o0o % O0 - oooO0oo0oOOOO
   if 100 - 100: oO - O0 % oOo0oooo00o * I1i1i1ii + oooO0oo0oOOOO
   if 88 - 88: OoooooooOO - i111I * O0 * OoooooooOO . OoooooooOO
   if 33 - 33: IiiIII111ii + IiiIIiiI11 * oOo0oooo00o / iIii1I11I1II1 - oooO0oo0oOOOO
  oOiIi1IIIi1 = { 'deviceid' : iIIi1i1 , 'automaintenance' : I1111IIi , 'storageinfolastpopup' : Ooo , 'fullautofreq' : iii , 'fullautocache' : ooOOOoOooOoO , 'fullautopackages' : III1IiiI , 'fullautothumb' : IIIII11I1IiI , 'cacheinclude_genesis' : ooO00OO0 , 'cacheinclude_navix' : OOOOoo0Oo , 'cacheinclude_youtube' : I1iI1iIi111i , 'cacheinclude_ivue' : I1I1I , 'cacheinclude_salts' : o0o0o0oO0oOO , 'cacheinclude_pulsar' : Ii11I1 , 'totaltempfiles' : oO0OOOO0 , 'totalspacegained' : I11iiI1i1 , 'lastbuildcheck' : oO0 , 'buildupdate' : oOo0O0o00o }
  if 54 - 54: IiiIII111ii / I1i1i1ii . oOo0oooo00o % IiiIIiiI11
  if 57 - 57: i11iIiiIii . O00o0o0000o0o - oO - oOo0oooo00o + II1Ii1iI1i
  if 63 - 63: II1Ii1iI1i * IiiIIiiI11
  with open ( O0O , 'w' ) as OOO00O :
   json . dump ( oOiIi1IIIi1 , OOO00O )
   OOO00O . close
   if 69 - 69: O0 . i111I
 except :
  if 49 - 49: oooO0oo0oOOOO - IIIII
  pass
  if 74 - 74: iIii1I11I1II1 * O00o0o0000o0o + II1Ii1iI1i / i1IIi / II111iiii . ooO0oo0oO0
  if 62 - 62: OoooooooOO * oooO0oo0oOOOO
oOOOoo0O0oO = str ( iiI1IiI ( 3400000511170344040 ) )
iIII1I111III = str ( iiI1IiI ( 13281251946689640 ) )
II = str ( iiI1IiI ( 10671040787093401628309229544054446898021653365987242101 ) )
o0o0O0O00oOOo = str ( iiI1IiI ( 69150464576736304288905009 ) )
iIIIiIi = str ( iiI1IiI ( 604749529580314795900374215312831791 ) )
I1i1I1II = str ( iiI1IiI ( 2147777190397934400065 ) )
if 100 - 100: oooO0oo0oOOOO / o0oOoO00o % II111iiii % ooO0oo0oO0 % I1i1i1ii
O00oO000O0O = str ( iiI1IiI ( 153602222665677990893023546055877026668326449094363582037501591738390924181764188878177568091504078998837196125307879221562544406625843871437059176 ) )
if 18 - 18: IiiIIiiI11 - I1i1i1ii . IiiIII111ii . iIii1I11I1II1
if 2 - 2: I1i1i1ii . i111I
O0ooooOOoo0O = str ( iiI1IiI ( 636043595498406984087267985324424431387932914792 ) )
II1IiiIi1i = str ( iiI1IiI ( 8392585944576975151 ) )
iiI11ii1I1 = str ( iiI1IiI ( 162827160447592187926340604243052654435323643982952 ) )
if 82 - 82: II111iiii % IIIII / i111I + II1Ii1iI1i / o0oOoO00o / IiiIII111ii
if 70 - 70: oOo0oooo00o
if 59 - 59: o0oOoO00o % oOo0oooo00o
if 6 - 6: iIii1I11I1II1 % i11iIiiIii % O00o0o0000o0o
if 93 - 93: oooOOOOO * OoooooooOO + i1iIIi1
def oO00O00o0OOO0 ( url ) :
 if 33 - 33: O0 * o0oOoO00o - IiiIII111ii % IiiIII111ii
 if 18 - 18: IiiIII111ii / ooO0oo0oO0 * IiiIII111ii + IiiIII111ii * i11iIiiIii * O00o0o0000o0o
 iI = urllib2 . Request ( url )
 iI . add_header ( 'User-Agent' , I1i1I1II )
 if 11 - 11: i1iIIi1 / II1Ii1iI1i - oooOOOOO * OoooooooOO + OoooooooOO . II1Ii1iI1i
 try :
  o00O = urllib2 . urlopen ( iI )
  if 26 - 26: oO % O00o0o0000o0o
 except HTTPError , Iii111II :
  if 76 - 76: oooOOOOO * IiiIIiiI11
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , str ( Iii111II . code ) , "" , "" )
  writelog('@Ares: HTTP Error: ' + str ( Iii111II . code ))
  writelog(url)
  return ( 'downloadfailed' )
  if 52 - 52: I1i1i1ii
 except URLError , Iii111II :
  if 19 - 19: oooO0oo0oOOOO
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , str ( Iii111II . reason ) , "" , "" )
  writelog('@Ares: URL Error: ' + str ( Iii111II . reason ))
  writelog(url)
  return ( 'downloadfailed' )
 except IOError , Iii111II :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , str ( Iii111II . errno ) + " - " + str ( Iii111II . strerror ) , "" , "" )
  writelog('@Ares: IO Error: ' + str ( Iii111II . errno ) + ' - ' + str ( Iii111II . strerror ))
  writelog(url)
  return ( 'downloadfailed' )
 except Exception , Iii111II :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , str ( type ( Iii111II . reason ) ) + " - " + str ( type ( Iii111II . reason ) ) , "" , "" )
  writelog('@Ares: Download Error: ' + str ( type ( Iii111II . reason ) ) + ' - ' + str ( type ( Iii111II . reason ) ))
  writelog(url)
  return ( 'downloadfailed' )
  if 25 - 25: oO / i1iIIi1
 except :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , "Unspecified Error (sorry)" , "" , "" )
  writelog('@Ares: Download Error: Unspecified')
  writelog(url)
  return ( 'downloadfailed' )
  if 31 - 31: I1i1i1ii . O0 % oooO0oo0oOOOO . o0oOoO00o + oooOOOOO
  if 71 - 71: IiiIII111ii . II111iiii
 try :
  IiII1I11i1I1I = o00O . read ( )
  if 62 - 62: OoooooooOO . IIIII
 except socket . timeout :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , "Socket Timeout" , "" , "" )
  writelog('@Ares: Download Error: Socket Timeout')
  return ( 'downloadfailed' )
  if 61 - 61: II1Ii1iI1i - I1i1i1ii - i1IIi
  if 25 - 25: O0 * IIIII + O00o0o0000o0o . o0oOoO00o . o0oOoO00o
 except socket . error :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , "Socket Error" , "" , "" )
  writelog('@Ares: Download Error: Socket Error')
  return ( 'downloadfailed' )
  if 58 - 58: oooO0oo0oOOOO
  if 53 - 53: i1IIi
  if 59 - 59: o0oOoO00o
 return ( IiII1I11i1I1I )
 if 81 - 81: II1Ii1iI1i - II1Ii1iI1i . IiiIIiiI11
 if 73 - 73: IIIII % i11iIiiIii - oooO0oo0oOOOO
 if 7 - 7: O0 * i11iIiiIii * oO + i1iIIi1 % i111I - i1iIIi1
 if 39 - 39: ooO0oo0oO0 * I1i1i1ii % I1i1i1ii - OoooooooOO + o0oOoO00o - IIIII
 if 23 - 23: i11iIiiIii
def II1iIi11 ( url ) :
 if 12 - 12: oO + i11iIiiIii * iIii1I11I1II1 / O00o0o0000o0o . IIIII
 if 5 - 5: i1IIi + oooOOOOO / o0oOoO00o . IiiIIiiI11 / IIIII
 iI = urllib2 . Request ( url )
 iI . add_header ( 'User-Agent' , O0oo0OO0 )
 if 32 - 32: oooO0oo0oOOOO % iIii1I11I1II1 / i1IIi - oooO0oo0oOOOO
 try :
  o00O = urllib2 . urlopen ( iI )
  if 7 - 7: IiiIII111ii * i111I - i1iIIi1 + I1i1i1ii * oooO0oo0oOOOO % i111I
 except HTTPError , Iii111II :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , str ( Iii111II . code ) )
  writelog('@Ares: HTTP Error: ' + str ( Iii111II . code ))
  return ( 'downloadfailed' )
  if 15 - 15: II1Ii1iI1i % oooO0oo0oOOOO * IIIII
 except URLError , Iii111II :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , str ( Iii111II . reason ) , "" , "" )
  writelog('@Ares: URL Error: ' + str ( Iii111II . reason ))
  return ( 'downloadfailed' )
  if 81 - 81: i1iIIi1 - iIii1I11I1II1 - i1IIi / IiiIII111ii - O0 * IIIII
 except IOError , Iii111II :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , str ( Iii111II . errno ) + " - " + str ( Iii111II . strerror ) , "" , "" )
  writelog('@Ares: IO Error: ' + str ( Iii111II . errno ) + ' - ' + str ( Iii111II . strerror ))
  return ( 'downloadfailed' )
 except Exception , Iii111II :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , str ( type ( Iii111II . reason ) ) + " - " + str ( type ( Iii111II . reason ) ) , "" , "" )
  writelog('@Ares: Download Error: ' + str ( type ( Iii111II . reason ) ) + ' - ' + str ( type ( Iii111II . reason ) ))
  return ( 'downloadfailed' )
  if 20 - 20: oOo0oooo00o % oooOOOOO
 except socket . timeout :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , "Socket Timeout" , "" , "" )
  writelog('@Ares: Download Error: Socket Timeout')
  return ( 'downloadfailed' )
  if 19 - 19: O00o0o0000o0o % oooOOOOO + i1iIIi1 / IiiIII111ii . i1iIIi1
  if 12 - 12: i1IIi + i1IIi - O00o0o0000o0o * ooO0oo0oO0 % ooO0oo0oO0 - II111iiii
 except socket . error :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , "Socket Error" , "" , "" )
  writelog('@Ares: Download Error: Socket Error')
  return ( 'downloadfailed' )
  if 52 - 52: i1iIIi1 . IiiIIiiI11 + IiiIII111ii
  if 38 - 38: i1IIi - II111iiii . IiiIII111ii
 except :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , "Unspecified Error (sorry)" , "" , "" )
  writelog('@Ares: Download Error: Unspecified')
  return ( 'downloadfailed' )
  if 58 - 58: oooO0oo0oOOOO . IiiIIiiI11 + II1Ii1iI1i
  if 66 - 66: IiiIIiiI11 / oOo0oooo00o * OoooooooOO + OoooooooOO % IIIII
 try :
  IiII1I11i1I1I = o00O . read ( )
  if 49 - 49: oOo0oooo00o - i11iIiiIii . IiiIII111ii * oO % IiiIIiiI11 + i1IIi
 except socket . timeout :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , "Socket Timeout" , "" , "" )
  writelog('@Ares: Download Error: Socket Timeout')
  return ( 'downloadfailed' )
  if 71 - 71: o0oOoO00o
  if 38 - 38: oOo0oooo00o % II1Ii1iI1i + O00o0o0000o0o . i11iIiiIii
 except socket . error :
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Download Error" , "Socket Error" , "" , "" )
  writelog('@Ares: Download Error: Socket Error')
  return ( 'downloadfailed' )
  if 53 - 53: i11iIiiIii * IiiIIiiI11
  if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOoO00o / II111iiii % ooO0oo0oO0
 return ( IiII1I11i1I1I )
 if 38 - 38: i1iIIi1 - I1i1i1ii / IiiIIiiI11
 if 66 - 66: O0 % O00o0o0000o0o + i11iIiiIii . II1Ii1iI1i / oO + O00o0o0000o0o
 if 86 - 86: o0oOoO00o
 if 5 - 5: oooOOOOO * II1Ii1iI1i
try :
 if 5 - 5: IiiIII111ii
 if 90 - 90: IiiIII111ii . i1iIIi1 / oO - IIIII
 with open ( O0O , 'r' , 0 ) as OOO00O :
  oOiIi1IIIi1 = json . load ( OOO00O )
  if 40 - 40: OoooooooOO
 #iIIi1i1 = oOiIi1IIIi1 [ 'deviceid' ]
 I1i1i1 = str ( oOiIi1IIIi1 [ 'lastbuildcheck' ] )
 if 73 - 73: O0 * IiiIIiiI11 + oO + i1iIIi1
except :
 if 40 - 40: II111iiii . II1Ii1iI1i * IiiIII111ii + I1i1i1ii + I1i1i1ii
 if 9 - 9: IIIII % OoooooooOO . oOo0oooo00o % IIIII
 writelog('@ares: failed to read config')
 exit ( )
 if 32 - 32: i11iIiiIii
 if 31 - 31: iIii1I11I1II1 / i111I / O00o0o0000o0o
 if 41 - 41: ooO0oo0oO0
try :
 if 10 - 10: ooO0oo0oO0 / ooO0oo0oO0 / IiiIII111ii . IiiIII111ii
 with open ( i1i1II , 'r' , 0 ) as OOO00O :
  try :
   oOiIi1IIIi1 = json . load ( OOO00O )
  except :
   oOiIi1IIIi1 = ""
   if 98 - 98: ooO0oo0oO0 / oooO0oo0oOOOO . O0 + i111I
 try :
  ii = oOiIi1IIIi1 [ 'buildname' ]
  writelog('@ares: buildinstallconfig: buildname: ' + ii)
 except :
  pass
  if 25 - 25: OoooooooOO - oooO0oo0oOOOO . oooO0oo0oOOOO * oOo0oooo00o
  if 81 - 81: IiiIIiiI11 + oooOOOOO
 try :
  o0oo0 = str ( oOiIi1IIIi1 [ 'installedversion' ] )
  writelog('@ares: buildinstallconfig: installedversion: ' + o0oo0)
 except :
  pass
  if 97 - 97: II1Ii1iI1i % O00o0o0000o0o
except :
 pass
 if 25 - 25: ooO0oo0oO0 % O00o0o0000o0o . O00o0o0000o0o
 if 55 - 55: i1iIIi1 - IIIII + II111iiii + IiiIIiiI11 % oO
 if 41 - 41: i1IIi - IIIII - oO
 if 8 - 8: i111I + IiiIII111ii - o0oOoO00o % ooO0oo0oO0 % o0oOoO00o * oOo0oooo00o
try :
 if 9 - 9: ooO0oo0oO0 - i11iIiiIii - I1i1i1ii * oO + i1iIIi1
 iIIII = os . path . join ( o0OoOoOO00 , 'settings.xml' )
 iIIIiiI1i1i = open ( iIIII , 'r' )
 iIII = iIIIiiI1i1i . read ( )
 iIIIiiI1i1i . close ( )
 if 70 - 70: IiiIIiiI11 / iIii1I11I1II1
 Oo0oooO0oO = oo ( iIII , 'checkbuildupdate" value="' , '"' )
 IiIiII1 = oo ( iIII , 'buildupdatefreq" value="' , '"' )
 if 21 - 21: O0 % oooOOOOO . oooO0oo0oOOOO / II111iiii + oooOOOOO
 writelog(' ')
 writelog('@ares: checkbuildupdate = ' + Oo0oooO0oO)
 writelog('@ares: buildupdatefreq = ' + IiIiII1)
 writelog(' ')
 if 53 - 53: oOo0oooo00o - oooO0oo0oOOOO - oOo0oooo00o * IiiIIiiI11
except :
 if 71 - 71: O0 - iIii1I11I1II1
 pass
 if 12 - 12: I1i1i1ii / o0oOoO00o
 if 42 - 42: ooO0oo0oO0
try :
 if Oo0oooO0oO == "true" :
  if 19 - 19: oOo0oooo00o % O00o0o0000o0o * iIii1I11I1II1 + oooO0oo0oOOOO
  iii11I = "no"
  iiIii ( 'buildupdate' , "no" )
  if 50 - 50: IiiIIiiI11 + O0 + oO . II111iiii / o0oOoO00o
  try :
   if 17 - 17: oO % iIii1I11I1II1 - iIii1I11I1II1
   if 78 - 78: IiiIIiiI11 + IIIII . i1iIIi1 - IiiIIiiI11 . oO
   oO0 = datetime . datetime . strptime ( I1i1i1 , '%Y-%m-%d' ) . date ( )
   writelog('@ares: lastbuildcheck = ' + str ( oO0 ))
   if 30 - 30: oooO0oo0oOOOO + i111I % oO * IiiIIiiI11 / ooO0oo0oO0 - IIIII
   if 64 - 64: iIii1I11I1II1
   if 21 - 21: ooO0oo0oO0 . II111iiii
  except :
   writelog('@ares: lastbuildcheck not found - defaulting to today')
   oO0 = datetime . date . today ( )
   iii11I = "yes"
   if 54 - 54: II111iiii % II111iiii
   if 86 - 86: O0 % oO * i1iIIi1 * iIii1I11I1II1 * i1IIi * IIIII
  OOOoOOO0oO = datetime . date . today ( ) - oO0
  if 28 - 28: i1iIIi1 + i11iIiiIii / IIIII % II1Ii1iI1i % ooO0oo0oO0 - O0
  if 54 - 54: i1IIi + II111iiii
  if 83 - 83: O00o0o0000o0o - oooO0oo0oOOOO + I1i1i1ii
  writelog('@ares: lastbuildcheck = ' + str ( oO0 ))
  writelog('@ares: dayssincelastrun = ' + str ( OOOoOOO0oO . days ))
  if 5 - 5: oO
  if 46 - 46: oooOOOOO
  if iii11I == "yes" :
   if 45 - 45: i1iIIi1
   i1 = "buildupdate"
   writelog('@ares: build update check triggered')
   i1111 = "yes"
   if 21 - 21: oOo0oooo00o . IiiIII111ii . I1i1i1ii / ooO0oo0oO0 / IiiIII111ii
   if 17 - 17: I1i1i1ii / I1i1i1ii / IIIII
  elif IiIiII1 == "0" and OOOoOOO0oO . days >= 1 :
   if 1 - 1: i1IIi . i11iIiiIii % I1i1i1ii
   i1 = "buildupdate"
   writelog('@ares: build update check triggered')
   i1111 = "yes"
   if 82 - 82: iIii1I11I1II1 + ooO0oo0oO0 . iIii1I11I1II1 % oooOOOOO / oO . oO
  elif IiIiII1 == "1" and OOOoOOO0oO . days >= 7 :
   if 14 - 14: o0oOoO00o . I1i1i1ii . IIIII + OoooooooOO - I1i1i1ii + oooOOOOO
   i1 = "buildupdate"
   writelog('@ares: build update check triggered')
   i1111 = "yes"
   if 9 - 9: oO
  elif IiIiII1 == "2" and OOOoOOO0oO . days >= 31 :
   if 59 - 59: oooO0oo0oOOOO * II111iiii . O0
   i1 = "buildupdate"
   writelog('@ares: build update check triggered')
   i1111 = "yes"
   if 56 - 56: oO - IiiIIiiI11 % oooO0oo0oOOOO - o0oOoO00o
  else :
   if 51 - 51: O0 / i1iIIi1 * iIii1I11I1II1 + O00o0o0000o0o + o0oOoO00o
   writelog('@ares: build update check not triggered')
   if 98 - 98: iIii1I11I1II1 * O00o0o0000o0o * I1i1i1ii + i1iIIi1 % i11iIiiIii % O0
   if 27 - 27: O0
   if 79 - 79: o0oOoO00o - IIIII + o0oOoO00o . oOo0oooo00o
   if 28 - 28: i1IIi - IiiIIiiI11
   if 54 - 54: IiiIIiiI11 - O0 % I1i1i1ii
  if i1111 == "yes" :
   if 73 - 73: O0 . II1Ii1iI1i + oooO0oo0oOOOO - IIIII % IIIII . IIIII
   try :
    if 17 - 17: oO - OoooooooOO % oO . oooOOOOO / i11iIiiIii % IiiIIiiI11
    with open ( i1i1II , 'r' , 0 ) as OOO00O :
     try :
      oOiIi1IIIi1 = json . load ( OOO00O )
     except :
      oOiIi1IIIi1 = ""
      if 28 - 28: IIIII
    try :
     ii = oOiIi1IIIi1 [ 'buildname' ]
     writelog('@ares: buildinstallconfig: buildname: ' + ii)
    except :
     ii = "0"
     if 58 - 58: II1Ii1iI1i
     if 37 - 37: ooO0oo0oO0 - iIii1I11I1II1 / O00o0o0000o0o
    try :
     i11 = oOiIi1IIIi1 [ 'canupdate' ]
     writelog('@ares: buildinstallconfig: canupdate: ' + i11)
    except :
     i11 = "0"
     if 73 - 73: i11iIiiIii - oooOOOOO
     if 25 - 25: OoooooooOO + oooOOOOO * O00o0o0000o0o
    try :
     OoO0ooO = oOiIi1IIIi1 [ 'buildurl' ]
     writelog('@ares: buildinstallconfig: buildurl: ' + OoO0ooO)
    except :
     OoO0ooO = "0"
     if 51 - 51: IiiIIiiI11 / i1iIIi1 * II1Ii1iI1i . IiiIIiiI11 / O00o0o0000o0o / i11iIiiIii
     if 21 - 21: oOo0oooo00o / O00o0o0000o0o + oO + OoooooooOO
    try :
     o0oo0 = str ( oOiIi1IIIi1 [ 'installedversion' ] )
     writelog('@ares: buildinstallconfig: installedversion: ' + o0oo0)
    except :
     o0oo0 = "0"
     if 91 - 91: i11iIiiIii / i1IIi + IiiIIiiI11 + i1iIIi1 * i11iIiiIii
   except :
    if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + IIIII * IiiIII111ii . oooOOOOO
    writelog('@ares: could not find buildinstall info')
    if 52 - 52: i1iIIi1 + O0 . IiiIIiiI11 . O00o0o0000o0o . i111I
    if 97 - 97: oooO0oo0oOOOO / IiiIIiiI11
   writelog('@ares: canupdate: ' + i11)
   if 71 - 71: II111iiii / i1IIi . O00o0o0000o0o % OoooooooOO . II1Ii1iI1i
   if 41 - 41: i1IIi * II111iiii / OoooooooOO . I1i1i1ii
   if i11 == "yes" or i11 == "Yes" :
    if 83 - 83: IiiIIiiI11 . O0 / ooO0oo0oO0 / I1i1i1ii - II111iiii
    oO0oO0 = "Error"
    if 14 - 14: IiiIIiiI11
    oOOOOo0oo0O = II1iIi11 ( OoO0ooO )
    if 13 - 13: oooO0oo0oOOOO % II1Ii1iI1i . O00o0o0000o0o / ooO0oo0oO0 % I1i1i1ii . OoooooooOO
    if oOOOOo0oo0O <> "downloadfailed" :
     if 22 - 22: oooOOOOO / i11iIiiIii
     writelog('@ares: wizarddata ok')
     if 62 - 62: i111I / O00o0o0000o0o
     oOOOOo0oo0O = oOOOOo0oo0O . replace ( '\n' , '' ) . replace ( '\r' , '' )
     if 7 - 7: OoooooooOO . oooOOOOO
     writelog('@ares: scanning wizarddata...')
     if 53 - 53: oO % oO * o0oOoO00o + II1Ii1iI1i
     Oooo00 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)".+?ersion="(.+?)"' ) . findall ( oOOOOo0oo0O )
     if 6 - 6: oO - i1iIIi1 * I1i1i1ii . IiiIIiiI11 / O0 * i1iIIi1
     for II11iI111i1 , Oo00OoOo , ii1ii111 , i11111I1I , ii1 , Oo0000oOo in Oooo00 :
      if 31 - 31: IIIII . IiiIII111ii * i1iIIi1 + i11iIiiIii * oOo0oooo00o
      if II11iI111i1 == ii :
       if 93 - 93: O00o0o0000o0o / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * IIIII
       oO0oO0 = str ( Oo0000oOo )
       if 64 - 64: II111iiii + O0 / iIii1I11I1II1 / ooO0oo0oO0 . i1iIIi1 % oooOOOOO
       writelog('@ares: buildname found')
       writelog('@ares: installedversion: ' + o0oo0)
       writelog('@ares: buildcurrentversion: ' + oO0oO0)
       if 50 - 50: iIii1I11I1II1 - oooOOOOO + I1i1i1ii
       if o0oo0 <> oO0oO0 :
        if 69 - 69: O0
        writelog('@ares: build update found')
        i1 = "buildupdate"
        oOOoo00O0O = "yes"
        iiIii ( 'buildupdate' , "yes" )
        if 85 - 85: i1iIIi1 / O0
       else :
        if 18 - 18: o0oOoO00o % O0 * O00o0o0000o0o
        writelog('@ares: build up to date')
        i1 = "none"
        if 62 - 62: IiiIII111ii . oooOOOOO . OoooooooOO
    else :
     if 11 - 11: I1i1i1ii / IIIII
     writelog('@ares: wizarddata download failed')
     oO0oO0 = "Error: wizarddata download failed"
     if 73 - 73: i1IIi / i11iIiiIii
     if 58 - 58: ooO0oo0oO0 . II111iiii + oOo0oooo00o - i11iIiiIii / II111iiii / O0
     if 85 - 85: II1Ii1iI1i + I1i1i1ii
    I1II = str ( datetime . date . today ( ) )
    if 27 - 27: II111iiii / oO . I1i1i1ii
    writelog(' ')
    writelog('@ares: timenow: ' + I1II)
    if 9 - 9: i1iIIi1 - O00o0o0000o0o - IiiIIiiI11
    iIIII = os . path . join ( o0OoOoOO00 , 'settings.xml' )
    iIIIiiI1i1i = open ( iIIII , 'r' )
    iIII = iIIIiiI1i1i . read ( )
    iIIIiiI1i1i . close ( )
    if 82 - 82: oooOOOOO - oooOOOOO + II1Ii1iI1i
    II111Ii1i1 = re . sub ( r'(<setting id="lastbuildcheck" value=").*(")' , r'<setting id="lastbuildcheck" value="%s" />' % I1II , iIII )
    II111Ii1i1 = re . sub ( r'(<setting id="buildlatestversion" value=").*(")' , r'<setting id="buildlatestversion" value="%s" />' % oO0oO0 , II111Ii1i1 )
    if 98 - 98: i111I . i111I * oOo0oooo00o * II111iiii * IiiIII111ii
    iIIIiiI1i1i = open ( iIIII , 'w' )
    iIIIiiI1i1i . write ( II111Ii1i1 )
    iIIIiiI1i1i . close ( )
    if 92 - 92: ooO0oo0oO0
    if 40 - 40: II1Ii1iI1i / oooOOOOO
    try :
     if 79 - 79: i111I - iIii1I11I1II1 + oO - IiiIII111ii
     iiIii ( 'lastbuildcheck' , str ( datetime . date . today ( ) ) )
     if 93 - 93: II111iiii . oooO0oo0oOOOO - ooO0oo0oO0 + II1Ii1iI1i
    except :
     if 61 - 61: II111iiii
     i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
     i11O0oo0OO0oOOOo . ok ( "Error" , "Error writing config" , "" , "" )
     if 15 - 15: i11iIiiIii % oooO0oo0oOOOO * IIIII / IiiIII111ii
     if 90 - 90: IiiIIiiI11
     if 31 - 31: I1i1i1ii + O0
   else :
    if 87 - 87: i1iIIi1
    i1 = "none"
    if 45 - 45: i111I / OoooooooOO - IiiIIiiI11 / oO % oooOOOOO
    if 83 - 83: oooO0oo0oOOOO . iIii1I11I1II1 - oooOOOOO * i11iIiiIii
    if 20 - 20: i1IIi * IiiIII111ii + II111iiii % o0oOoO00o % oOo0oooo00o
    if 13 - 13: ooO0oo0oO0
    if 60 - 60: O00o0o0000o0o * oooO0oo0oOOOO
    if 17 - 17: I1i1i1ii % ooO0oo0oO0 / O00o0o0000o0o . oooOOOOO * I1i1i1ii - II111iiii
    if 41 - 41: oO
    if 77 - 77: IiiIII111ii
except :
 if 65 - 65: II111iiii . oooO0oo0oOOOO % oOo0oooo00o * i111I
 pass
 if 38 - 38: II1Ii1iI1i / IiiIIiiI11 % ooO0oo0oO0
 if 11 - 11: IiiIIiiI11 - oOo0oooo00o + II111iiii - iIii1I11I1II1
try :
 if 7 - 7: oooOOOOO - IIIII / II111iiii * oO . IiiIIiiI11 * IiiIIiiI11
 iIIII = os . path . join ( IiII1IiiIiI1 , 'addon.xml' )
 iIIIiiI1i1i = open ( iIIII , 'r' )
 O0O0oOOo0O = iIIIiiI1i1i . read ( )
 if 19 - 19: o0oOoO00o / IiiIII111ii % o0oOoO00o % IiiIIiiI11 * oooOOOOO
 ii1oOoO0o0ooo = oo ( O0O0oOOo0O , '" version="' , '"' )
 if 86 - 86: O00o0o0000o0o * O0 * oooOOOOO
 if 51 - 51: II111iiii + oooOOOOO . i1IIi . O00o0o0000o0o + II1Ii1iI1i * oooO0oo0oOOOO
 if 72 - 72: oOo0oooo00o + oOo0oooo00o / II111iiii . OoooooooOO % oO
 if 49 - 49: oOo0oooo00o . i111I - ooO0oo0oO0 * OoooooooOO . ooO0oo0oO0
 if 2 - 2: OoooooooOO % I1i1i1ii
 if 63 - 63: oooO0oo0oOOOO % iIii1I11I1II1
 Oo00OoOo = O00oO000O0O + iIIIiIi
 if 39 - 39: IiiIIiiI11 / II111iiii / O00o0o0000o0o % oooO0oo0oOOOO
 IiII1I11i1I1I = oO00O00o0OOO0 ( Oo00OoOo )
 if 89 - 89: IiiIII111ii + OoooooooOO + IiiIII111ii * i1IIi + iIii1I11I1II1 % IIIII
 if 59 - 59: I1i1i1ii + i11iIiiIii
 if "currentversion" not in IiII1I11i1I1I :
  if 88 - 88: i11iIiiIii - i1iIIi1
  if 67 - 67: I1i1i1ii . ooO0oo0oO0 + II1Ii1iI1i - OoooooooOO
  if 70 - 70: I1i1i1ii / II111iiii - iIii1I11I1II1 - IiiIIiiI11
  Oo00OoOo = oOOOoo0O0oO + II + iIIIiIi
  if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - IIIII
  if 30 - 30: II1Ii1iI1i
  if 21 - 21: i11iIiiIii / IiiIII111ii % I1i1i1ii * O0 . IIIII - iIii1I11I1II1
  IiII1I11i1I1I = oO00O00o0OOO0 ( Oo00OoOo )
  if 26 - 26: II111iiii * II1Ii1iI1i
  if 10 - 10: II111iiii . IiiIIiiI11
  if "currentversion" not in IiII1I11i1I1I :
   if 32 - 32: oO . oooOOOOO . OoooooooOO - i111I + oOo0oooo00o
   pass
   if 88 - 88: IiiIIiiI11
   if 19 - 19: II111iiii * oooOOOOO + oO
   if 65 - 65: I1i1i1ii . IiiIII111ii . i111I . IiiIIiiI11 - I1i1i1ii
   if 19 - 19: i11iIiiIii + IiiIIiiI11 % i1iIIi1
   if 14 - 14: i111I . II111iiii . IIIII / oO % O00o0o0000o0o - i1iIIi1
   if 67 - 67: IIIII - I1i1i1ii . i1IIi
 I1I1iI = oo ( IiII1I11i1I1I , '<currentversion=' , '>' )
 I1iIi1iiIIiI = oo ( IiII1I11i1I1I , '<updatefile=' , '>' )
 if 81 - 81: i111I * II1Ii1iI1i . I1i1i1ii
 if 11 - 11: i11iIiiIii - oOo0oooo00o . oOo0oooo00o
 if 31 - 31: I1i1i1ii / ooO0oo0oO0 * i1IIi . II1Ii1iI1i
 writelog('---- A R E S  C H E C K  U P D A T E ---')
 writelog(' ')
 writelog('@ares: wizard version = ' + str ( ii1oOoO0o0ooo ))
 writelog('@ares: latestversion = ' + str ( I1I1iI ))
 if 57 - 57: I1i1i1ii + iIii1I11I1II1 % i1IIi % oooO0oo0oOOOO
 if 83 - 83: o0oOoO00o / i11iIiiIii % iIii1I11I1II1 . IIIII % oOo0oooo00o . OoooooooOO
 if 94 - 94: oO + iIii1I11I1II1 % i111I
 if 93 - 93: oO - I1i1i1ii + iIii1I11I1II1 * o0oOoO00o + IiiIII111ii . IiiIIiiI11
 if 49 - 49: OoooooooOO * IIIII - ooO0oo0oO0 . oOo0oooo00o
 if I1I1iI <> ii1oOoO0o0ooo :
  if 89 - 89: i1iIIi1 + oO * i1iIIi1 / i1iIIi1
  if 46 - 46: i111I
  O0000 = oo ( iIII , 'autoupdate" value="' , '"' )
  if 64 - 64: II111iiii - oooO0oo0oOOOO
  writelog('@ares: autoupdatesetting = ' + str ( O0000 ))
  if 68 - 68: i1iIIi1 - I1i1i1ii - iIii1I11I1II1 / II1Ii1iI1i + I1i1i1ii - i111I
  if O0000 == "true" :
   if 75 - 75: IiiIIiiI11 / o0oOoO00o % iIii1I11I1II1 . OoooooooOO % OoooooooOO % II111iiii
   writelog('@ares: downloading update ' + str ( O0000 ))
   writelog('@ares: updateurl =  ' + str ( I1iIi1iiIIiI ))
   if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % IIIII * IIIII * O00o0o0000o0o
   IiI1I11iIii = xbmcgui . DialogProgress ( )
   IiI1I11iIii . create ( "Ares Wizard" , "Please Wait, Installing Update" , '' , '' )
   IiI1I11iIii . update ( 0 )
   if 63 - 63: IiiIIiiI11 * IIIII * oO - oOo0oooo00o - oO
   o0oo = os . path . join ( iIiiiI , 'ares.zip' )
   urllib . urlretrieve ( I1iIi1iiIIiI , o0oo )
   if 52 - 52: O00o0o0000o0o + O00o0o0000o0o . II111iiii
   time . sleep ( 3 )
   IiI1I11iIii . update ( 50 )
   if 34 - 34: OoooooooOO . O0 / oOo0oooo00o * II1Ii1iI1i - O00o0o0000o0o
   IiiiI = zipfile . ZipFile ( o0oo , 'r' )
   if 42 - 42: i1IIi . oooO0oo0oOOOO / i1IIi + oO
   try :
    for O0o0O0OO00o in IiiiI . infolist ( ) :
     IiiiI . extract ( O0o0O0OO00o , iIiiiI1IiI1I1 )
     if 92 - 92: o0oOoO00o + IiiIII111ii / ooO0oo0oO0 % i111I % oooOOOOO . OoooooooOO
     if 52 - 52: i1iIIi1 / i11iIiiIii - I1i1i1ii . oooOOOOO % iIii1I11I1II1 + o0oOoO00o
     if 71 - 71: oOo0oooo00o % IIIII * II1Ii1iI1i . O0 / oO . O00o0o0000o0o
   except Exception , Iii111II :
    writelog( str ( Iii111II ))
    if 58 - 58: ooO0oo0oO0 / oOo0oooo00o
    if 44 - 44: I1i1i1ii
   writelog( '@ares: update finished ')
   if 54 - 54: oO - IIIII - IiiIII111ii . iIii1I11I1II1
   IiI1I11iIii . update ( 100 )
   IiI1I11iIii . close
   if 79 - 79: oO . i111I
  else :
   if 40 - 40: o0oOoO00o + ooO0oo0oO0 . o0oOoO00o % i1iIIi1
   writelog('@ares: update bypassed (auto-updates turned off)')
   if 15 - 15: oO * ooO0oo0oO0 % O00o0o0000o0o * iIii1I11I1II1 - i11iIiiIii
except :
 if 60 - 60: oooO0oo0oOOOO * IiiIII111ii % i111I + oOo0oooo00o
 pass
 if 52 - 52: i1IIi
 if 84 - 84: oO / oooOOOOO
 if 86 - 86: II1Ii1iI1i * II111iiii - O0 . II1Ii1iI1i % iIii1I11I1II1 / I1i1i1ii
try :
 if 11 - 11: oooO0oo0oOOOO * oOo0oooo00o + O00o0o0000o0o / O00o0o0000o0o
 iiii1I1 = os . path . join ( o0OoOoOO00 , 'userdata' )
 IIIiIiI11iIi = os . path . join ( o0OoOoOO00 , 'backup' )
 if 89 - 89: O0
 shutil . rmtree ( iiii1I1 )
 shutil . rmtree ( IIIiIiI11iIi )
except :
 pass
 if 2 - 2: O00o0o0000o0o . O00o0o0000o0o + O00o0o0000o0o * o0oOoO00o
 if 100 - 100: ooO0oo0oO0 % oO / IIIII
 if 30 - 30: ooO0oo0oO0 - I1i1i1ii - IiiIIiiI11
 if 81 - 81: o0oOoO00o . OoooooooOO + I1i1i1ii * i1iIIi1
 if 74 - 74: i1IIi + O0 + ooO0oo0oO0
 if 5 - 5: ooO0oo0oO0 * II1Ii1iI1i
ii1I11iIiIII1 = os . path . join ( iI111iI , 'statsicon_c_0.png' )
oOO0OOOOoooO = os . path . join ( iI111iI , 'statsicon_c_1.png' )
i1ii11 = os . path . join ( iI111iI , 'statsicon_c_2.png' )
ii1i = os . path . join ( iI111iI , 'statsicon_c_3.png' )
IIi = os . path . join ( iI111iI , 'statsicon_p_0.png' )
oo0OO = os . path . join ( iI111iI , 'statsicon_p_1.png' )
IiiI11i1I = os . path . join ( iI111iI , 'statsicon_p_2.png' )
OOo0 = os . path . join ( iI111iI , 'statsicon_p_3.png' )
iiIii1IIi = os . path . join ( iI111iI , 'statsicon_t_0.png' )
ii1IiIiI1 = os . path . join ( iI111iI , 'statsicon_t_1.png' )
OOOoOo00O = os . path . join ( iI111iI , 'statsicon_t_2.png' )
O0ooOo0o0Oo = os . path . join ( iI111iI , 'statsicon_t_3.png' )
if 71 - 71: iIii1I11I1II1 - I1i1i1ii . oooO0oo0oOOOO % OoooooooOO + I1i1i1ii
IIi11I1 = os . path . join ( iI111iI , 'servicebox.png' )
if 49 - 49: II111iiii - oooO0oo0oOOOO / IIIII
if 74 - 74: IIIII - I1i1i1ii + i1IIi . oooO0oo0oOOOO + I1i1i1ii - IIIII
Ii = 10
if 15 - 15: O0 + O0 / ooO0oo0oO0 . oOo0oooo00o * IIIII - O00o0o0000o0o
OOoO0ooOO = 10
iii1IIII1iii11I = 7
if 97 - 97: OoooooooOO - IiiIII111ii
if 58 - 58: iIii1I11I1II1 + O0
if 30 - 30: i1iIIi1 % IiiIIiiI11 * I1i1i1ii - O00o0o0000o0o * oO % i1iIIi1
if 46 - 46: i11iIiiIii - O0 . oOo0oooo00o
if 100 - 100: oooO0oo0oOOOO / o0oOoO00o * IiiIIiiI11 . O0 / I1i1i1ii
if 83 - 83: IiiIII111ii
if 48 - 48: II111iiii * I1i1i1ii * IiiIII111ii
try :
 I1111IIi = oOiIi1IIIi1 [ 'automaintenance' ]
except :
 I1111IIi = "never"
 if 50 - 50: oooOOOOO % i1IIi
 if 21 - 21: OoooooooOO - iIii1I11I1II1
try :
 iii = oOiIi1IIIi1 [ 'fullautofreq' ]
except :
 iii = "never"
 if 93 - 93: oOo0oooo00o - o0oOoO00o % II1Ii1iI1i . II1Ii1iI1i - i1iIIi1
 if 90 - 90: i1iIIi1 + II111iiii * O00o0o0000o0o / oO . o0oOoO00o + o0oOoO00o
 if 40 - 40: i1iIIi1 / II1Ii1iI1i % i11iIiiIii % O00o0o0000o0o / oooO0oo0oOOOO
 if 62 - 62: i1IIi - II1Ii1iI1i
 if 62 - 62: i1IIi + ooO0oo0oO0 % oooOOOOO
 if 28 - 28: O00o0o0000o0o . i1IIi
 if 10 - 10: i111I / ooO0oo0oO0
 if 15 - 15: IiiIIiiI11 . II1Ii1iI1i / IiiIIiiI11 * IIIII - oooO0oo0oOOOO % O00o0o0000o0o
if I1111IIi <> "0" and I1111IIi <> "never" :
 if 57 - 57: O0 % II1Ii1iI1i % oOo0oooo00o
 if 45 - 45: O00o0o0000o0o + II111iiii * i11iIiiIii
 try :
  IiIIi1I1I11Ii = str ( oOiIi1IIIi1 [ 'storageinfolastpopup' ] )
  if 64 - 64: OoooooooOO
  Ooo = datetime . datetime . strptime ( IiIIi1I1I11Ii , '%Y-%m-%d' ) . date ( )
 except :
  Ooo = datetime . date . today ( )
  if 81 - 81: O00o0o0000o0o - O0 * OoooooooOO
  if 23 - 23: II111iiii / oOo0oooo00o
  if 28 - 28: ooO0oo0oO0 * i1iIIi1 - i111I
  if 19 - 19: IIIII
  if 67 - 67: O0 % iIii1I11I1II1 / oooOOOOO . i11iIiiIii - oO + O0
 OOOoOOO0oO = datetime . date . today ( ) - Ooo
 if 27 - 27: I1i1i1ii
 if 89 - 89: II111iiii / oOo0oooo00o
 if 14 - 14: I1i1i1ii . oooO0oo0oOOOO * i1iIIi1 + II111iiii - i1iIIi1 + I1i1i1ii
 if I1111IIi == "daily" and OOOoOOO0oO . days < 1 :
  writelog('maintenance reminder not due')
  exit ( )
 if I1111IIi == "monthly" and OOOoOOO0oO . days < 31 :
  writelog('maintenance reminder not due')
  exit ( )
 if I1111IIi == "weekly" and OOOoOOO0oO . days < 7 :
  writelog('maintenance reminder not due')
  exit ( )
  if 18 - 18: oOo0oooo00o - o0oOoO00o - oooO0oo0oOOOO - oooO0oo0oOOOO
 i1 = "maintenance"
 if 54 - 54: ooO0oo0oO0 + oooO0oo0oOOOO / IiiIIiiI11 . oooO0oo0oOOOO * II1Ii1iI1i
 try :
  if 1 - 1: II1Ii1iI1i * i111I . i1IIi / ooO0oo0oO0 . O00o0o0000o0o + ooO0oo0oO0
  iiIii ( 'storageinfolastpopup' , str ( datetime . date . today ( ) ) )
  if 17 - 17: ooO0oo0oO0 + i111I / oO / IiiIIiiI11 * I1i1i1ii
 except :
  if 29 - 29: i111I % OoooooooOO * oOo0oooo00o / II111iiii - oOo0oooo00o
  i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
  i11O0oo0OO0oOOOo . ok ( "Error" , "Error writing config" , "" , "" )
  if 19 - 19: i11iIiiIii
  if 54 - 54: II111iiii . IIIII
  if 73 - 73: II1Ii1iI1i . oooO0oo0oOOOO
 o0o0oOoOO0 ( Iii1ii1II11i )
 II1i11i1iIi11 = total_files
 oo0O0oO0O0O = total_size / 1024 / 1024
 I1111I1iII11 ( )
 o0o0oOoOO0 ( iIiiiI )
 oOo0O = total_files
 I11iIiii1 = total_size / 1024 / 1024
 if 1 - 1: oO
 IiiiI1 = "None"
 if 100 - 100: oOo0oooo00o . oO % i1IIi . i1iIIi1
 if 79 - 79: i111I % I1i1i1ii / iIii1I11I1II1 + II1Ii1iI1i * i111I
 if 30 - 30: OoooooooOO / IIIII + IiiIIiiI11 / O00o0o0000o0o * O0
 if I11iIiii1 >= 180 :
  iIiII = OOo0
  IiiiI1 = "Clear packages"
  if 19 - 19: oooOOOOO
 if I11iIiii1 >= 70 and I11iIiii1 < 180 :
  iIiII = IiiI11i1I
  if 78 - 78: I1i1i1ii % o0oOoO00o
 if I11iIiii1 >= 1 and I11iIiii1 < 70 :
  iIiII = oo0OO
  if 39 - 39: O00o0o0000o0o + oooO0oo0oOOOO - iIii1I11I1II1 - o0oOoO00o
 if I11iIiii1 == 0 :
  iIiII = IIi
  if 7 - 7: oooOOOOO . II1Ii1iI1i / O00o0o0000o0o . I1i1i1ii * IIIII - II111iiii
  if 37 - 37: IiiIII111ii . II1Ii1iI1i / O0 * IiiIIiiI11
  if 7 - 7: i111I * IIIII + II111iiii % i11iIiiIii
  if 8 - 8: i1iIIi1 * O0
 if oo0O0oO0O0O >= 2000 :
  OOoO = O0ooOo0o0Oo
  IiiiI1 = "Clear thumbnails"
  if 18 - 18: iIii1I11I1II1 + ooO0oo0oO0 - I1i1i1ii + OoooooooOO * OoooooooOO
 if oo0O0oO0O0O >= 1000 and oo0O0oO0O0O < 2000 :
  OOoO = OOOoOo00O
  if 41 - 41: i1iIIi1 . ooO0oo0oO0 + oooO0oo0oOOOO
 if oo0O0oO0O0O >= 1 and oo0O0oO0O0O < 1000 :
  OOoO = ii1IiIiI1
  if 100 - 100: oO + i111I
 if oo0O0oO0O0O == 0 :
  OOoO = iiIii1IIi
  if 73 - 73: i1IIi - IiiIII111ii % i1iIIi1 / i111I
  if 40 - 40: O00o0o0000o0o * i1iIIi1 - oooO0oo0oOOOO / oooOOOOO / i11iIiiIii
  if 83 - 83: O00o0o0000o0o / IiiIII111ii - i11iIiiIii . iIii1I11I1II1 + ooO0oo0oO0
  if 59 - 59: O0 % ooO0oo0oO0
 if tempandcachesize >= 200 :
  O0o00O0Oo0 = ii1i
  IiiiI1 = "Clear cache\\temp"
  if 58 - 58: O0
 if tempandcachesize >= 100 and tempandcachesize < 200 :
  O0o00O0Oo0 = i1ii11
  if 78 - 78: i111I % oooOOOOO * i1IIi
 if tempandcachesize >= 1 and tempandcachesize < 100 :
  O0o00O0Oo0 = oOO0OOOOoooO
  if 66 - 66: oO . oooO0oo0oOOOO + o0oOoO00o . iIii1I11I1II1
 if tempandcachesize == 0 :
  O0o00O0Oo0 = ii1I11iIiIII1
  if 51 - 51: IIIII . ooO0oo0oO0
  if 45 - 45: i1IIi - ooO0oo0oO0 / O0 . O00o0o0000o0o
  if 5 - 5: o0oOoO00o . iIii1I11I1II1 % iIii1I11I1II1
  if 56 - 56: OoooooooOO - IIIII - i1IIi
  if 8 - 8: IiiIII111ii / I1i1i1ii . oooO0oo0oOOOO + O00o0o0000o0o / i11iIiiIii
  if 31 - 31: i1iIIi1 - iIii1I11I1II1 + IiiIIiiI11 . ooO0oo0oO0 / oooOOOOO % iIii1I11I1II1
  if 6 - 6: oooOOOOO * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + o0oOoO00o / i1IIi
  if 53 - 53: IIIII + iIii1I11I1II1
class oOooo0Oo ( xbmcgui . WindowDialog ) :
 def __init__ ( self ) :
  I1 = 10
  Ii = 10
  self . addControl ( xbmcgui . ControlImage ( x = 240 , y = 200 , width = 143 , height = 200 , filename = I11i ) )
  self . addControl ( xbmcgui . ControlImage ( x = 384 , y = 200 , width = 650 , height = 200 , filename = IIi11I1 ) )
  if 66 - 66: ooO0oo0oO0
  if 28 - 28: oooOOOOO - oooOOOOO . i1IIi - i1iIIi1 + oooO0oo0oOOOO . oooOOOOO
  if i1 == "maintenance" :
   if 54 - 54: II1Ii1iI1i - IiiIII111ii
   if 3 - 3: oooO0oo0oOOOO - ooO0oo0oO0
   self . addControl ( xbmcgui . ControlImage ( x = 295 , y = 275 , width = 25 , height = 127 , filename = iIiII ) )
   self . addControl ( xbmcgui . ControlImage ( x = 325 , y = 275 , width = 25 , height = 127 , filename = O0o00O0Oo0 ) )
   self . addControl ( xbmcgui . ControlImage ( x = 355 , y = 275 , width = 25 , height = 127 , filename = OOoO ) )
   if 16 - 16: oOo0oooo00o + i1iIIi1 / o0oOoO00o
   self . addControl ( xbmcgui . ControlLabel ( x = 400 , y = 215 , width = 630 , height = 25 , label = "There are " + str ( oOo0O ) + " package files detected, taking up " + str ( I11iIiii1 ) + "MB of storage." , alignment = 6 ) )
   if 82 - 82: oooOOOOO * i11iIiiIii % II111iiii - OoooooooOO
   self . addControl ( xbmcgui . ControlLabel ( x = 400 , y = 240 , width = 630 , height = 25 , label = "There are " + str ( tempandcachefiles ) + " cache\\temp files detected, taking up " + str ( tempandcachesize ) + "MB of storage." , alignment = 6 ) )
   if 90 - 90: ooO0oo0oO0 . oOo0oooo00o * i1IIi - i1IIi
   self . addControl ( xbmcgui . ControlLabel ( x = 400 , y = 265 , width = 630 , height = 25 , label = "You have " + str ( II1i11i1iIi11 ) + " thumbnails, taking up " + str ( oo0O0oO0O0O ) + "MB of storage." , alignment = 6 ) )
   if 16 - 16: oooO0oo0oOOOO * i1IIi - o0oOoO00o . oooOOOOO % IIIII / o0oOoO00o
   if 14 - 14: iIii1I11I1II1 * IiiIII111ii * O00o0o0000o0o / iIii1I11I1II1 * oooOOOOO / IIIII
   self . addControl ( xbmcgui . ControlLabel ( x = 400 , y = 310 , width = 630 , height = 25 , label = "Recommended action: " + IiiiI1 , alignment = 6 ) )
   if 77 - 77: i111I + IiiIII111ii + IiiIII111ii * oO / OoooooooOO . oO
   if 62 - 62: i1IIi - i1IIi
  if i1 == "buildupdate" :
   if 69 - 69: II1Ii1iI1i % oOo0oooo00o - IIIII
   self . addControl ( xbmcgui . ControlLabel ( x = 400 , y = 210 , width = 630 , height = 25 , label = "An update is available for your build" , alignment = 6 ) )
   self . addControl ( xbmcgui . ControlLabel ( x = 400 , y = 240 , width = 630 , height = 25 , label = "(" + ii + ")" , alignment = 6 ) )
   if 38 - 38: iIii1I11I1II1 + i11iIiiIii / i11iIiiIii % i111I / i1iIIi1 % oO
   self . addControl ( xbmcgui . ControlLabel ( x = 400 , y = 280 , width = 630 , height = 25 , label = "Installed Version: " + o0oo0 , alignment = 6 ) )
   if 7 - 7: oooOOOOO * oooO0oo0oOOOO + i1IIi + i11iIiiIii + ooO0oo0oO0 % oooO0oo0oOOOO
   self . addControl ( xbmcgui . ControlLabel ( x = 405 , y = 305 , width = 630 , height = 25 , label = "Current Version: " + oO0oO0 , alignment = 6 ) )
   if 62 - 62: o0oOoO00o - oO * II1Ii1iI1i - i11iIiiIii % i1iIIi1
   if 52 - 52: O00o0o0000o0o % oOo0oooo00o - i11iIiiIii
   if 30 - 30: IiiIIiiI11 / i111I + oOo0oooo00o
  self . button_ares = xbmcgui . ControlButton ( 525 , 355 , 200 , 35 , "Launch Ares Wizard" , focusTexture = iI1Ii11111iIi , noFocusTexture = IiII , alignment = 6 )
  self . addControl ( self . button_ares )
  if 6 - 6: IiiIIiiI11 . IIIII + oO . IiiIII111ii
  self . button_close = xbmcgui . ControlButton ( 735 , 355 , 130 , 35 , "Close (" + str ( I1 ) + ")" , focusTexture = iI1Ii11111iIi , noFocusTexture = IiII , alignment = 6 )
  self . addControl ( self . button_close )
  self . setFocus ( self . button_close )
  if 70 - 70: i111I
  self . button_close . controlRight ( self . button_ares )
  self . button_close . controlLeft ( self . button_ares )
  self . button_ares . controlRight ( self . button_close )
  self . button_ares . controlLeft ( self . button_close )
  if 46 - 46: IIIII - i1IIi
  if 46 - 46: IiiIII111ii % oO
  if 72 - 72: iIii1I11I1II1
  if 45 - 45: ooO0oo0oO0 - o0oOoO00o % IiiIII111ii
  if 38 - 38: IiiIII111ii % I1i1i1ii - OoooooooOO
  if 87 - 87: i111I % oooO0oo0oOOOO
  if 77 - 77: iIii1I11I1II1 - i1IIi . oOo0oooo00o
 def onAction ( self , action ) :
  if action == OOoO0ooOO :
   self . close ( )
   if 26 - 26: o0oOoO00o * oooOOOOO . i1IIi
   if 59 - 59: O0 + i1IIi - o0oOoO00o
   if 62 - 62: i11iIiiIii % I1i1i1ii . oooOOOOO . I1i1i1ii
   if 84 - 84: i11iIiiIii * i111I
 def onControl ( self , control ) :
  if control == self . button_close :
   try :
    if 18 - 18: I1i1i1ii - oO - II1Ii1iI1i / IiiIII111ii - O0
    iiIii ( 'buildupdate' , "no" )
    iiIii ( 'lastbuildcheck' , str ( datetime . date . today ( ) ) )
    if 30 - 30: O0 + O00o0o0000o0o + II111iiii
   except :
    if 14 - 14: o0oOoO00o / I1i1i1ii - iIii1I11I1II1 - oOo0oooo00o % i1iIIi1
    i11O0oo0OO0oOOOo = xbmcgui . Dialog ( )
    i11O0oo0OO0oOOOo . ok ( "Error" , "Error writing config" , "" , "" )
   self . close ( )
   if 49 - 49: i1iIIi1 * oOo0oooo00o / o0oOoO00o / ooO0oo0oO0 * iIii1I11I1II1
  if control == self . button_ares :
   xbmc . executebuiltin ( "RunAddon(script.areswizard)" )
   OOoO00ooO . close ( )
   self . close ( )
   if 12 - 12: i1iIIi1 % oooO0oo0oOOOO + oOo0oooo00o - i1IIi . oO / oooO0oo0oOOOO
   if 51 - 51: I1i1i1ii . oooO0oo0oOOOO
   if 73 - 73: OoooooooOO . oooO0oo0oOOOO / IiiIII111ii % oO
   if 65 - 65: oooOOOOO - oooO0oo0oOOOO - oO
   if 42 - 42: II111iiii * oooO0oo0oOOOO % i1IIi - oO % oooOOOOO
   if 36 - 36: i11iIiiIii / oOo0oooo00o * O00o0o0000o0o * O00o0o0000o0o + oO * IIIII
if __name__ == '__main__' :
 if 32 - 32: i111I
 if i1 == "maintenance" or i1 == "buildupdate" :
  if 50 - 50: i1iIIi1 + i1IIi
  OOoO00ooO = oOooo0Oo ( )
  OOoO00ooO . show ( )
  if 31 - 31: oO
  OoOOo00 = time . time ( )
  I1 = Ii
  while ( time . time ( ) - OoOOo00 <= Ii ) :
   I1 = I1 - 1
   OOoO00ooO . button_close . setLabel ( "Close (" + str ( I1 ) + ")" )
   xbmc . sleep ( 1000 )
   if I1 < 1 :
    OOoO00ooO . close ( )
    sys . exit ( )
  OOoO00ooO . doModal ( )
  del OOoO00ooO # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
