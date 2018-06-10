# -*- coding: utf-8 -*-
import urllib
import urllib2
import datetime
import re
import os
import base64
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib
import sys
import xbmc
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP

try:
    import json
except:
    import simplejson as json
	
try:
    import jsunpack
except:
    pass
	
	
import SimpleDownloader as downloader
addon = xbmcaddon.Addon(id='plugin.video.kractosbr')
addon_version = addon.getAddonInfo('version')
profile = xbmc.translatePath(addon.getAddonInfo('profile').decode('utf-8'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8'))
favorites = os.path.join(profile, 'favorites')
history = os.path.join(profile, 'history')
plugin = addon.getSetting('plugin')
REV = os.path.join(profile, 'list_revision')
icon = os.path.join(home, 'icon.png')
icon2 = os.path.join(home, 'icon2.png')
batman = os.path.join(home,'batman.png')
chaves = os.path.join(home,'chaves.png')
FANART = os.path.join(home, 'fanart.jpg')
source_file = os.path.join(profile, 'source_file')
functions_dir = profile
dialog=xbmcgui.Dialog()

def getUrl(url, cookieJar=None,post=None, timeout=20, headers=None):


	cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
	opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
	#opener = urllib2.install_opener(opener)
	req = urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
	if headers:
		for h,hv in headers:
			req.add_header(h,hv)

	response = opener.open(req,post,timeout=timeout)
	link=response.read()
	response.close()
	return link;

	
def abrir_url(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return link
	except IOError as e:#     except urllib2.HTTPError, e:
		dialog.notification('','Não foi possivel acessar o servidor.',icon)
		sys.exit(0)
###
#RESOLVERS DIA 30/05/2018
###
def kratos_resolver_vk_com(url):
	link = getUrl(url)
	names = []
	urls = []
	match = re.compile('"url(\d+)":"(.+?)"').findall(link)
	for namea,url in match:
		names.append(namea)
		urls.append(url)	
	opcao = xbmcgui.Dialog().select('-=Kratos Kodi Br =-', names)
	if opcao>= 0:
		repro = urls[opcao].replace('\/','/')		
		liz = xbmcgui.ListItem(name, iconImage=iconimage)
		liz.setPath(repro)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)					
	else:
		sys.exit()
		
###
#RESOLVERS DIA 18/05/2018
###
	
def RedeCanais_Tv(url):
	basi = url.replace("https","http")
	link = abrir_url(basi)
	urls = []
	names = []
	player = re.compile('<iframe name="Player".*?src="(.*?)".*?allowFullScreen>\s*</iframe>').findall(link)[0]
	a = abrir_url(player)
	soup =  BeautifulSoup(a,convertEntities=BeautifulSoup.HTML_ENTITIES)
	matchs = soup.find('div',{'class':"player"}).findAll('div')
	for d in matchs:
		urls.append(d.form['action'])
		names.append(d.a.text)
	opcao = xbmcgui.Dialog().select('-=Kratos Kodi Br =-', names)
	if opcao>= 0:
		e = urls[opcao]
		if 'vib.php?canal' in e:
			f = abrir_url(e)
			res = re.compile("""height=100%"\s*width="100%"\s*src="(http:?[^'"\<>\[\]]+)""").findall(f)[0]
			reproduzir = res+'|Referer='+player
			liz = xbmcgui.ListItem(name, iconImage=iconimage)
			liz.setPath(reproduzir)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
		elif 'jw.php?canal' in e:
			f = abrir_url(e)
			res = re.compile('file.*?"(.*?)",').findall(f)[0]
			reproduzir = res+'|Referer='+player
			liz = xbmcgui.ListItem(name, iconImage=iconimage)
			liz.setPath(reproduzir)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
		
	else:
		sys.exit()	
###
#RESOLVERS DIA 10/05/2018
###
def Pre_link_estream(url):		
	try:
		a = abrir_url(url)
		urls = []
		names = []
		soup =  BeautifulSoup(a,convertEntities=BeautifulSoup.HTML_ENTITIES)	
		soups = soup.findAll('source')
		for d in soups:
			urls.append(d['src'])
			names.append('Resolução Desconhecida' if d.get('label')==None else d.get('label').split('x')[1])
		opcao = xbmcgui.Dialog().select('-=Kratos Kodi Br =-', names)
		if opcao>= 0:	
			e = urls[opcao]
			liz = xbmcgui.ListItem(name, iconImage=iconimage)
			liz.setPath(e)
			xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	except: pass			
def Pre_link_animesonlineq(url):		
	link = abrir_url(url)
	r ='<link itemprop="embedURL" href="(.*?)">'
	match = re.compile(r).findall(link)
	for urls in match:
		liz = xbmcgui.ListItem(name, iconImage=iconimage)
		liz.setPath(urls)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
		
		
###
#RESOLVERS DIA 10/05/2018
###		
def Pre_link_rede_canais(url):		
	uri = url.replace("https","http")
	link = abrir_url(uri)
	r ='<iframe name="Player".*?src="(.*?)".*?allowFullScreen>\s*</iframe>'
	match = re.compile(r).findall(link)
	for urls in match:
		links = abrir_url(urls)
		matchs = re.compile('file: "(.*?)",').findall(links)[0]
		liz = xbmcgui.ListItem(name, iconImage=iconimage)
	#	liz.setInfo(type='Video', infoLabels={'Title':name})
	#	liz.setProperty("IsPlayable","true")
		plays  = matchs+"|Referer="+urls
		liz.setPath(plays)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
def Pre_link_rapidvideo(url):		
	link  = abrir_url(url)
	urls = []
	names = []
	soup = BeautifulSoup(link)
	for i in soup.findAll('a'):
		if '&q=' in i['href']:
			urls.append(i['href'])
			names.append(i.text)
	opcao = xbmcgui.Dialog().select('-=Kratos Kodi Br =-', names)
	if opcao>= 0:
		a = abrir_url(urls[opcao])
		match = re.compile('<source src="(.*?)"').findall(a)[0]
		liz = xbmcgui.ListItem(name, iconImage=iconimage)
		liz.setPath(match)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	else:
		sys.exit()
def Pre_link_pipocao(url):
	link  = abrir_url(url)
	urls = []
	names = []
	m18 = re.compile(r"createEmbedSource.*?'','.*?','.*?',.*?,'(.*?)','.*?','.*?','360p','.*?>").findall(link)
	m22 = re.compile(r"createEmbedSource.*?'','.*?','.*?',.*?,'.*?','(.*?)','.*?','.*?','720p','.*?>").findall(link)
	m37 = re.compile(r"createEmbedSource.*?'','.*?','.*?',.*?,'.*?','.*?','(.*?)','.*?','.*?','1080p'.*?>").findall(link)
	if ('=m18' in link):
		uri = m18
		nome = '360p'
		urls.append(uri)
		names.append(nome)
	if ('=m22' in link):
		uri = m22
		nome = '720p'
		urls.append(uri)
		names.append(nome)
	if ('=m37' in link):
		uri = m37
		nome = '1080p'
		urls.append(uri)
		names.append(nome)
	opcao = xbmcgui.Dialog().select('-=Kratos Kodi Br =-', names)
	if opcao>= 0:
		link = urls[opcao]
		linkss = link[0]
		liz = xbmcgui.ListItem(name, iconImage=iconimage)
		liz.setPath(linkss)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	else:
		sys.exit()
		
def Pre_link_netcine(url):
	a = abrir_url(url)
	b = re.compile('<iframe src="(.*?)"').findall(a)[0]
	link = abrir_url(b)
	reg = re.compile('file: "(.*?)"').findall(link)
	items_url = []
	items_name = []
	for url in reg:
		if 'ALTO' in url:
			items_names = 'Qualidade Alta'
			items_name.append(items_names)
			items_url.append(url)
		elif 'BAIXO' in url:
			items_names = 'Qualidade Baixa'
			items_name.append(items_names)		
			items_url.append(url)		
	opcao = xbmcgui.Dialog().select('-=Kratos Kodi Br =-', items_name)
	if opcao>= 0:
		linkss = items_url[opcao] 
		linkss+='|Referer=http://netcine.us/'
		liz = xbmcgui.ListItem(name, iconImage=iconimage)
	#	liz.setInfo(type='Video', infoLabels={'Title':name})
	#	liz.setProperty("IsPlayable","true")
		liz.setPath(linkss)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	else:
		sys.exit()

		
def Pre_link_mmfilmes(url):
	ref = url
	referer = [('Referer',url)]#getUrl(page_value,headers=referer)
	a =  getUrl(url, headers=referer)
	base_mmf = 'http://player.mmfilmes.tv'
	b = re.compile("addiframe.*?'(.*?)'").findall(a)[0]
	c = getUrl(base_mmf+b, headers=referer)
	items_url = []
	items_name = []
	match = re.compile("{'file':'(.*?)'.*?'label").findall(c)
	for url in  set(match):
		if '360p' in url:
			items_names = '360p'
			items_name.append(items_names)
			items_url.append(url)
		elif '480p' in url:
			items_names = '480p'
			items_name.append(items_names)		
			items_url.append(url)	
		elif '720p' in url:
			items_names = '720p'
			items_name.append(items_names)		
			items_url.append(url)		
		elif '1080p' in url:
			items_names = '1080p'
			items_name.append(items_names)		
			items_url.append(url)		
			
	opcao = xbmcgui.Dialog().select('-=Kratos Kodi Br =-', items_name)
	if opcao>= 0:
		linkss = items_url[opcao] 
		linkss+='|Referer='+ref
		liz = xbmcgui.ListItem(name, iconImage=iconimage)
	#	liz.setInfo(type='Video', infoLabels={'Title':name})
	#	liz.setProperty("IsPlayable","true")
		liz.setPath(linkss)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	else:
		sys.exit()

def Pre_link_seuseriado(url):
	url = url.replace('#038;','').replace("https","http")
	referer = [('Referer','http://seuseriado.com/')]#'https://seuseriado.com/')]#getUrl(page_value,headers=referer)
	link =		''
	items_url = []
	items_name = []
	match = re.compile("'(https.*?)','(.*?)'").findall(link)
	for urls,names in match:
		urls = urls.replace('/r.php?','/redirect.php?')
		items_name.append(names)		
		items_url.append(urls)			
	opcao = xbmcgui.Dialog().select('-=Kratos Kodi Br =-', items_name)
	if opcao>= 0:
		linkss = items_url[opcao] 
		#linkss+='|Referer=http://www.mmfilmes.tv/'
		liz = xbmcgui.ListItem(name, iconImage=iconimage)
	#	liz.setInfo(type='Video', infoLabels={'Title':name})
	#	liz.setProperty("IsPlayable","true")
		liz.setPath(linkss)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	else:
		sys.exit()	
		
def Check_update():
	versao='10.0'
	Source_Update = os.path.join(home, 'Player_Kratos.py')
	base_update = abrir_url('https://raw.githubusercontent.com/brunolojino/listas/master/Kratos_Update.txt')
	check = re.compile("versao='(.*?)'").findall(base_update)[0]
	if versao==check:
		pass
	else:
		f = open(Source_Update, 'wb')
		f.write(base_update)
		f.close()
		dialog.ok('-=Kratos Kodi Br =-','Versão do player: '+versao,'Versão do player disponível: '+check,'Atualizando o player do add-on feche e abra novamente.')
		sys.exit(0) 

def post_page_free(url, data, headers):
    req = urllib2.Request(url, data, headers)
    page = urllib2.urlopen(req).read()
    return page
	
    		
def kratos_resolver_ok_ru(url):
	OPERA_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36 OPR/34.0.2036.50'
	qual_map = {'ultra': '2160', 'quad': '1440', 'full': '1080', 'hd': '720', 'sd': '480', 'low': '360', 'lowest': '240', 'mobile': '144'}
	ur = "http://www.ok.ru/dk"
	ra = re.compile('(?://|\.)(ok\.ru|odnoklassniki\.ru)/(?:videoembed|video)/(\d+)').findall(url)
	media_id  = ra[0][1]
	header = {"User-Agent": OPERA_USER_AGENT}
	urls = []
	names = []
	data = {'cmd': 'videoPlayerMetadata', 'mid': media_id}
	data = urllib.urlencode(data)
	html = post_page_free(ur, data, headers=header)
	json_data = json.loads(html)
	jsons = json_data['videos']
	jsons.reverse()
	for a in jsons:
		names.append(qual_map.get(a.get('name')))
		urls.append(a.get('url'))	
	opcao = xbmcgui.Dialog().select('-=Kratos Kodi Br =-', names)
	if opcao>= 0:
		repro = urls[opcao]
		repros = repro+'|User-Agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36 OPR/34.0.2036.50'
		liz = xbmcgui.ListItem(name, iconImage=iconimage)
	#	liz.setInfo(type='Video', infoLabels={'Title':name})
	#	liz.setProperty("IsPlayable","true")
		liz.setPath(repros)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	else:
		sys.exit(0)    
	
def Other(url):
	url2 = url
	liz = xbmcgui.ListItem(name, iconImage=iconimage)
	liz.setPath(url2)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)		

Rsolvers_Kratos = ['pipocao.com','redecanais.','netcine.us','mmfilmes.tv','rapidvideo.com','estream.nu','estream.to','animesonlineq.net','Other://','www.redecanais.tv','ok_ru','vk_com']	
def Resolvers(url,name,iconimage):   	
	Check_update()
	rURL = url.replace(';','')
	if 'pipocao.com' in rURL and not 'Other://' in rURL:
		link = rURL
		Pre_link_pipocao(link)		
	elif 'redecanais' in rURL and not 'Other://' in rURL and not 'www.redecanais.tv' in rURL:
		link = rURL
		Pre_link_rede_canais(link)
	elif 'netcine.us' in rURL and not 'Other://' in rURL:
		link = rURL
		xbmc.log(link)
		Pre_link_netcine(link)	
	elif 'mmfilmes.tv' in rURL and not 'Other://' in rURL:
		link = rURL
		xbmc.log(link)
		Pre_link_mmfilmes(link)					
	elif 'rapidvideo.com' in rURL and not 'Other://' in rURL:
		link = rURL
		xbmc.log(link)
		Pre_link_rapidvideo(link)				
	elif 'estream.nu' in rURL or 'estream.to' in rURL and not 'Other://' in rURL:
		link = rURL
		xbmc.log(link)
		Pre_link_estream(link)					
	elif 'animesonlineq.net' in rURL and not 'Other://' in rURL:
		link = rURL
		xbmc.log(link)
		Pre_link_animesonlineq(link)	
		
	elif 'www.redecanais.tv' in rURL and not 'Other://' in rURL:
		link = rURL
		link = link.replace('www.redecanais.tv','www.redecanais.link')
		RedeCanais_Tv(link)					
				
	elif 'ok_ru' in rURL and not 'Other://' in rURL:
		link = rURL.replace('ok_ru','ok.ru')
		kratos_resolver_ok_ru(link)					
						
	elif 'vk_com' in rURL and not 'Other://' in rURL:
		link = rURL.replace('vk_com','vk.com')
		kratos_resolver_vk_com(link)					
		
	elif 'Other://' in rURL:
		link = rURL
		link = link.replace('Other://','')
		Other(link)			

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
iconimage=None
fanart=FANART
try:
    url=urllib.unquote_plus(params["url"]).decode('utf-8')
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
