#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import urlresolver
import sys
from BeautifulSoup import BeautifulSoup


pluginhandle = int(sys.argv[1])

versao = '1.0'
addon_base = 'MEU-GUIA.TV'
addon_id = 'plugin.video.MEU-GUIA.TV'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.jpg'
icones = addonfolder + '/icon.png'
base = 'http://megafilmeshd21.net/'
base2 = 'https://meuguia.tv'
wizard_create = selfAddon.getSetting('wizard_create')
local_wizard = xbmc.translatePath(os.path.join(wizard_create))


############################################################################################################
#                                           LISTAR VIDEOS                                                
############################################################################################################
		
def contar_acessos():
	req = urllib2.Request('https://goo.gl/sb9b22')
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

	
def categorias(url):
	contar_acessos()
	link = abrir_url('https://meuguia.tv/')
	match = re.compile('<a href="(.*?)">\s*(.*?)<br />\s*<span class="metadados">(.*?)</span>').findall(link)
	for url,name,cate_name in match:
		name = name.replace('S&eacute;ries','Séries').replace('Document&aacute;rios','Documentários').replace('Not&iacute;','Notícias').replace('Notíciascias','Notícias')
		cate_name = cate_name.replace('Veja tudo que est&aacute; passando agora na TV!','Veja tudo que está passando agora na TV!')
		if selfAddon.getSetting('startup') == "0":
			addDir('[COLOR lime]\n|>   [/COLOR]'+'  [COLOR darkseagreen]%s[/COLOR]'%name+'   [COLOR lime]  < - >  [/COLOR]    ''[COLOR white]'+cate_name+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]',base2+url,2,artfolder + 'icon.png')
		elif selfAddon.getSetting('startup') == "1":
			addDir('[COLOR white]'+name+':[/COLOR]\n[COLOR darkseagreen]'+cate_name+'[/COLOR]\n',base2+url,2,artfolder + 'icon.png')


		
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin("Container.SetViewMode(51)")		
		
def listar_filmes(url):#title
	link  = abrir_url(url)
	match = re.compile('<a title=".*?" href="(.*?)">\s*<div class=.*?>(.*?)</div>\s*<div class=.*?><strong>(.*?)</strong>(.*?)</div>').findall(link)
	for url,name,hora,canal in match:
		#url = teste.a["href"]
		#img = teste.img["src"]
		#name = teste.a["title"]
		name = name.replace('|','').replace('amp;','').replace('','')
		hora = hora.replace('|','').replace('amp;','').replace('h',':')
		canal = canal.replace('|','').replace('amp;','').replace('','')
		canal = canal.replace('Max Prime *e','Max Prime').replace('HBO Plus *e','HBO Plus')
		if selfAddon.getSetting('startup') == "0":
			addDir('[COLOR lime]\n|>   [/COLOR]'+'[COLOR darkseagreen]%s[/COLOR]'%canal+'  [COLOR lime]  < - >  [/COLOR]''  [COLOR white]'+hora+'[/COLOR]  ''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR darkseagreen]'+name+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]',base2+url,99,artfolder + 'icon.png')
		elif selfAddon.getSetting('startup') == "1":
			addDir('[COLOR lime]'+name+'[/COLOR]\n[COLOR darkseagreen]'+hora+'[/COLOR]  | [COLOR white]'+canal+'[/COLOR]\n',base2+url,99,artfolder + 'icon.png')
	
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin("Container.SetViewMode(51)")	
	
############################################################################################################
#                                           PLAYER                                                
############################################################################################################		

def pegar_link(url): #98
	link  = abrir_url(url)
	cana = re.compile('<div style="font-size.*?">(.*?)</div>').findall(link)
	for canals in cana:
	    canals
	match = re.compile('\\.*?\\href="(.*?)">\s*<div class=.*?>(.*?)</div>\s*<div>\s*<div class=.*?>(.*?)</div>\s*<div class=.*?>(.*?)</div>').findall(link)
	for url,name,hora,cate in match:
		name = name.replace('&#8211; ','').replace('','').replace('','')
		cate = cate.replace('/',' | ')
		name = name.replace('Max Prime *e','Max Prime').replace('HBO Plus *e','HBO Plus').replace('h','[B]:[/B]')
		canals = canals.replace('Max Prime *e','Max Prime').replace('HBO Plus *e','HBO Plus')
		if selfAddon.getSetting('startup') == "0":
			addDir('[COLOR lime]\n|>   [/COLOR]'+'[COLOR darkseagreen]%s[/COLOR]'%canals+' [COLOR lime]  < - >  [/COLOR]'' [COLOR white]''[COLOR white]'+name+'[/COLOR]''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR darkseagreen]'+hora+'[/COLOR]''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR white]'+cate+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]',base2+url,96,artfolder + 'icon.png')
		elif selfAddon.getSetting('startup') == "1":
			addDir('[COLOR darkseagreen]'+name+'[/COLOR][COLOR lime]\
        '+hora+'[/COLOR]\n[COLOR white]'+canals+'[/COLOR]        '+cate,base2+url,96,artfolder + 'icon.png')
		
#		addDir('[COLOR lime]\n|>   [/COLOR]'+'[COLOR darkseagreen]%s[/COLOR]'%canals+' [COLOR lime]  < - >  [/COLOR]'' [COLOR white]''[COLOR white]'+name+'[/COLOR]''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR darkseagreen]'+hora+'[/COLOR]''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR white]'+cate+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]',base2+url,96,artfolder + 'icon.png')
		
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin("Container.SetViewMode(51)")	

		
#########

#		addDir('[COLOR lime]\n|>   [/COLOR]'+'[COLOR darkseagreen]%s[/COLOR]'%canals+' [COLOR lime]  < - >  [/COLOR]'' [COLOR white]''[COLOR white]'+name+'[/COLOR]''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR darkseagreen]'+hora+'[/COLOR]''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR white]'+cate+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]',base2+url,96,artfolder + 'icon.png')
			
#		addDir(name+'      \
 #      '+hora+'\n'+canals+'         '+cate,base2+url,96,artfolder + 'icon.png')	
#		addDir('[COLOR lime]\n|>   [/COLOR]'+'[COLOR darkseagreen]%s[/COLOR]'%canal+' [COLOR lime]  < - >  [/COLOR]''[COLOR white]'+data+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]','','',artfolder + 'icon.png',False)
#		addDir('[COLOR lime]\n|>   [/COLOR]'+'  [COLOR darkseagreen]%s[/COLOR]'%name+'   [COLOR lime]  < - >  [/COLOR]    ''[COLOR white]'+itnes+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]',base2+url,2,artfolder + 'icon.png')
 
def description1(url):# 5 
#	if 'description' in description:
	showText(addon_base,url)
	
def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return 
        except:
            pass	 
	
def re_me(data, re_patten):
    match = ''
    m = re.search(re_patten, data)
    if m != None:
        match = m.group(1)
    else:
        match = ''
    return match	        	
	

	
def pegar_player_trailer(url):
	link  = abrir_url(url)
	infos = re.compile('var str="(.*?)";').findall(link)
	for info in infos:
		infor = re.findall(r'<span class="small_data">(.*?)<span class="texto">',link,re.DOTALL)[0]
		infor = infor.replace('        	','').replace('        </span>','').replace('        <hr />','').replace('| ','').replace('        ','').replace('\n\n\n\n','').replace('mins',' - Minutos').replace(' ','')
		Direcao = re_me(link,'<span class="texto2"><strong>Dire&ccedil;&atilde;o:</strong><br />(.*?)</span>')
		Elenco = re_me(link,'<span class="texto2"><strong>Elenco:</strong><br />(.*?)</span>')
		addDir('[COLOR white]Detalhes do programa[/COLOR]','informaçao: '+infor+'\n\nDirecao: '+Direcao+'.\n\nElenco: '+Elenco+'\n\nDescriçao: '+info,5,artfolder + 'icon.png',False)
		addDir('                                                                        ',url,2,artfolder + 'icon.png',False)

	cana = re.compile('<span class="texto">(.*?)</span>').findall(link)
	for name in cana:
		addDir('[COLOR white]Próximas exibições[/COLOR]',url,2,artfolder + 'icon.png',False)
		addDir('                                                                        ',url,2,artfolder + 'icon.png',False)

		#addDir('                                                                        ',url,2,artfolder + 'icon.png',False)
	match = re.compile('<a>\s*(.*?)<br />\s*<span class="metadados">(.*?)</span>\s*</a>').findall(link)
	for data,canal in match:
		data = data.replace('Dom','Domingo').replace('Seg','Segunda-feira').replace('Ter','Terça-feira').replace('Qua','Quarta-feira').replace('Qui','Quinta-feira').replace('Sex','Sexta-feira').replace('Sáb','Sábado').replace(',',' , ')
		canal = canal.replace('Max Prime *e','Max Prime').replace('HBO Plus *e','HBO Plus')
		if selfAddon.getSetting('startup') == "0":
			addDir('[COLOR lime]\n|>   [/COLOR]'+'[COLOR darkseagreen]%s[/COLOR]'%canal+' [COLOR lime]  < - >  [/COLOR]''[COLOR white]'+data+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]','','',artfolder + 'icon.png',False)
		elif selfAddon.getSetting('startup') == "1":
			addDir('[COLOR darkseagreen][B]'+data+'[/COLOR]\n[COLOR white]'+canal+'[/COLOR][/B]','','',artfolder + 'icon.png',False)
		#		addDir('[COLOR lime]\n|>   [/COLOR]'+'[COLOR darkseagreen]%s[/COLOR]'%canal+' [COLOR lime]  < - >  [/COLOR]''[COLOR white]'+data+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]','','',artfolder + 'icon.png',False)
		
		
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin("Container.SetViewMode(51)")	
############################################################################################################
#                                           FUNÇOES FEITAS                                                 #
############################################################################################################		
def setViewMenu():
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		
		opcao = selfAddon.getSetting('menuVisu')
		
		if   opcao == '0': xbmc.executebuiltin("Container.SetViewMode(50)")
		elif opcao == '1': xbmc.executebuiltin("Container.SetViewMode(51)")
		elif opcao == '2': xbmc.executebuiltin("Container.SetViewMode(500)")
		
def setViewFilmes():
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
        categorias(url)
      #  teste = abrir_url('https://goo.gl/oKyPTl')	


		
	  
elif mode==2: listar_filmes(url)
elif mode==4: categorias(url)
elif mode==5: description1(url)

elif mode==99: pegar_link(url)
elif mode==98: pegar_link_google(url)
elif mode==97: pegar_player_Legendados(url)
elif mode==96: pegar_player_trailer(url)

#########################################          FIM
xbmcplugin.endOfDirectory(int(sys.argv[1]))