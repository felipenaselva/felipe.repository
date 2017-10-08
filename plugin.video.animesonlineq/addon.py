#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright 2014
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon

import urlresolver
from BeautifulSoup import BeautifulSoup



pluginhandle = int(sys.argv[1])

versao = '0.0.1'
addon_base = 'ANIMESONLINEQ'
addon_id = 'plugin.video.animesonlineq'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'
icones = addonfolder + '/icon.png'
base = 'http://megafilmeshd21.net/'
base2 = 'http://filmeseserieshd.org/categoria'
   


############################################################################################################
#                                           MENU ADDON                                                 
############################################################################################################

def CATEGORIES():
	addDir('[COLOR whitesmoke]GENEROS[/COLOR]','http://www.animesonlineq.net/generos.html',110,artfolder + 'generos.png')
	addDir('[COLOR whitesmoke]LEG  A  a  Z[/COLOR]','http://www.animesonlineq.net/animes-legendados.html',10,artfolder + 'legendados.png')
	addDir('[COLOR whitesmoke]DUB  A  a  Z[/COLOR]','http://www.animesonlineq.net/animes-dublados.html',11,artfolder + 'Dublados.png')
	addDir('[COLOR whitesmoke]LANÇAMENTOS[/COLOR]','http://www.animesonlineq.net/ultimos-lancamentos.html',2,artfolder + 'lanca.png')
	addDir(' ','-',97,' ',False)
	addDir('[COLOR whitesmoke]OPEN SETINGS[/COLOR]','-',80,icones,False)	
	
	
	setViewMenu()	
	

###################################################################################
#FUNCOES
'''
	    link  = abrir_url(url)		
		soup = BeautifulSoup(link)
		match = soup.findAll("div", {"id" : "content"})
	for teste in match:
		url = teste.a["href"]
		img = teste.img["src"]	
		name = teste.a["alt"].replace('Assistir ','')
		addDir(name,url,3,img)'''

############################################################################################################
#                                           OPEN SETINGS                                                
############################################################################################################	
def Addon_Settings():
    selfAddon.openSettings(sys.argv[0])

	
############################################################################################################
#                                           GENEROS                                                
############################################################################################################		
def generos(url):
	link  = abrir_url(url)
	texto = re.findall('<div class="gens" style="">(.*?)<div id="footer">',link,re.DOTALL)[0]
	match=re.compile(r'<a href="(.*?)">(.*?)</a>').findall(texto)
	for url,name in match:
	#	name  = url.text
		addDir('[COLOR white]%s[/COLOR]'%name,url,3,artfolder + 'generos.png')
        
	setViewMenu()	
############################################################################################################
#                                           CATEGORIAS ABCDE                                                
############################################################################################################	

def categorias_abc(url):
	link  = abrir_url(url)
	soup = BeautifulSoup(link)	
	generos = soup.find("div",{"id":"abasLegendados"})
	categorias = generos.findAll("li")
	#match = re.compile('<a href="(.*?)" title="(.*?)">.*?</a>').findall(link)
	for teste in categorias:
		url = teste.a["href"]
		name = teste.a["title"]
		#name = name.replace('Assistir','').replace(' - Todos os Episódios Online','').replace('Assistir Ao no','').replace('sfdfdsdsfddsf','')
		addDir('[COLOR white]%s[/COLOR]'%name.encode('utf8'),url,3,artfolder + 'legendados.png')
    
	setViewMenu()	
	
def categorias_abc2(url):
	link  = abrir_url(url)
	soup = BeautifulSoup(link)	
	generos = soup.find("div",{"id":"abasLegendados"})
	categorias = generos.findAll("li")
	#match = re.compile('<a href="(.*?)" title="(.*?)">.*?</a>').findall(link)
	for teste in categorias:
		url = teste.a["href"]
		name = teste.a["title"]
		#name = name.replace('Assistir','').replace(' - Todos os Episódios Online','').replace('Assistir Ao no','').replace('sfdfdsdsfddsf','')
		addDir('[COLOR white]%s[/COLOR]'%name.encode('utf8'),url,3,artfolder + 'Dublados.png')
    
	setViewMenu()	
############################################################################################################
#                                           LISTAR ANIMES                                                
############################################################################################################	
def listar_videos_dublados(url):#title
	link  = abrir_url(url)
	#soup = BeautifulSoup(link)	
	#match= soup.findAll("div", {"class" : "breadcrumb_last"})
	match = re.compile('<a href="(.*?)" >\s*<img src=".*?" data-src="(.*?)" width=".*?" alt="(.*?)">').findall(link)
	for url,img,name in match:
		#url = teste.at["href"]
		#img = teste.img["src"].replace('?1','')
		name = name.replace('Assistir','').replace(' - Todos os Episódios Online','').replace('Assistir Ao no','').replace('sfdfdsdsfddsf','')
		addDir('[COLOR white]%s[/COLOR]'%name,url,4,img)
	try:
		match = re.compile('<a href="(.*?)">(.*?)</a>').findall(link)
		for url,ref in match:
			if ' » ' in ref:
				addDir('[COLOR green]Próxima Página[/COLOR]',url,3,'',True)
	except:pass       
		
		
	setViewFilmes() 

############################################################################################################
#                                           LISTAR EPISODIOS                                                
############################################################################################################	
def listar_animes(url):
	link  = abrir_url(url)
	#teste = []
	soup = BeautifulSoup(link)	
	generos = soup.find("div",{"id":"listEpiAnime"})
	categorias = generos.findAll("li")
	#match = re.compile('<a href="(.*?)" title="(.*?)">.*?</a>').findall(link)
	for teste in categorias:
		url = teste.a["href"]
		name = teste.a["title"]
		addDir('[COLOR white]%s[/COLOR]'%name.encode('utf8'),url,99,iconimage,False)

    
	setViewFilmes() 	

############################################################################################################
#                                           LISTAR VIDEOS                                                
############################################################################################################				
def listar_videos(url):#title
	link  = abrir_url(url)
	#soup = BeautifulSoup(link)	
	#match= soup.findAll("div", {"class" : "breadcrumb_last"})
	match = re.compile('<a href="(.*?)">\s*<img src="(.*?)" width=".*?" alt="(.*?)">').findall(link)
	for url,img,name in match:
	    	#url = teste.at["href"]
		    #img = teste.img["src"].replace('?1','')
		    #name = teste.img["alt"]
		    addDir('[COLOR white]%s[/COLOR]'%name,url,99,img,False)
	try:
		match = re.compile('<a href="(.*?)">(.*?)</a>').findall(link)
		for url,ref in match:
			if ' » ' in ref:
				addDir('[COLOR green]Próxima Página[/COLOR]',url,2,'',True)
	except:pass
	
	setViewFilmes() 

############################################################################################################
#                                           PLAYER                                                
############################################################################################################		
def pegar_link(url):
	dp = xbmcgui.DialogProgress()
	dp.create(addon_base, 'abrindo link ','Por favor aguarde...')
	html = abrir_url(url)
	link = re.compile('<link itemprop="embedURL" href="(.*?)"').findall(html)[0]
#	link = link.replace('&autoplay=true','')
	print link
	playlist = xbmc.PlayList(1)
	playlist.clear()
	try:
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name})
		listitem.setProperty('mimetype', 'video/mp4')    
		playlist.add(link,listitem)
		xbmcPlayer = xbmc.Player()
		dp.close()
		xbmcPlayer.play(playlist)
	except:
	    pass			
############################################################################################################
#                                           FUNÇOES FEITAS                                                 #
############################################################################################################		
def setViewMenu() :
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		
		opcao = selfAddon.getSetting('menuVisu')
		
		if   opcao == '0': xbmc.executebuiltin("Container.SetViewMode(50)")
		elif opcao == '1': xbmc.executebuiltin("Container.SetViewMode(51)")
		elif opcao == '2': xbmc.executebuiltin("Container.SetViewMode(500)")
		
def setViewFilmes() :
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')

		opcao = selfAddon.getSetting('filmesVisu')

		if   opcao == '0': xbmc.executebuiltin("Container.SetViewMode(50)")
		elif opcao == '1': xbmc.executebuiltin("Container.SetViewMode(51)")
		elif opcao == '2': xbmc.executebuiltin("Container.SetViewMode(500)")
		elif opcao == '3': xbmc.executebuiltin("Container.SetViewMode(501)")
		elif opcao == '4': xbmc.executebuiltin("Container.SetViewMode(508)")
		elif opcao == '5': xbmc.executebuiltin("Container.SetViewMode(504)")
		elif opcao == '6': xbmc.executebuiltin("Container.SetViewMode(503)")
		elif opcao == '7': xbmc.executebuiltin("Container.SetViewMode(515)")
		
		
def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link



def addDir(name,url,mode,iconimage,pasta=True,total=1,plot=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="video", infoLabels={ "title": name, "plot": plot } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok

############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################
              
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


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)



###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################
#abrir_url('https://goo.gl/oKyPTl')


if mode==None or url==None or len(url)<1:
        print "aqui inica o addon  asdasdsadahlhlhhhjlljhljhjjklhkljhkhjhkhjhj"
        CATEGORIES()
        teste = abrir_url('https://goo.gl/oKyPTl')	
		
elif mode==1: categorias(url)
elif mode==10: categorias_abc(url)
elif mode==11: categorias_abc2(url)
elif mode==110: generos(url)
###########################         listar videos

elif mode==2: listar_videos(url)
elif mode==3: listar_videos_dublados(url)
elif mode==4: listar_animes(url)

###########################             OPEN SETINGS

elif mode==80: Addon_Settings()

#########################################          
###########################             player

elif mode==99: pegar_link(url)

#########################################          FIM
xbmcplugin.endOfDirectory(int(sys.argv[1]))