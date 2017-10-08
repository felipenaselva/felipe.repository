def pegar_link(url): #98
	link  = abrir_url(url)
	f = open(local_wizard,'a')
	cana = re.compile('<div style="font-size.*?">(.*?)</div>').findall(link)
	for canals in cana:
	    canals
		#canals.replace('Programação ','').replace(' | meuguia.TV','')
	f.write('\n\n\n<channels>\n    <channel>\n        <name>'+canals+'</name>\n        <thumbnail>aqui icone</thumbnail>\n        <fanart>aqui fanart</fanart>\n        <items>\n\n') 	
	match = re.compile('\\.*?\\href="(.*?)">\s*<div class=.*?>(.*?)</div>\s*<div>\s*<div class=.*?>(.*?)</div>\s*<div class=.*?>(.*?)</div>').findall(link)
	for url,name,hora,cate in match:
		#url = teste.a["href"]
		#img = teste.img["src"]
		#name = teste.a["title"]
		name = name.replace('&#8211; ','').replace('','').replace('','')
		#canals.replace('Programação','').replace('| meuguia.TV','')
		name = name.replace('Max Prime *e','Max Prime').replace('HBO Plus *e','HBO Plus')
		canals = canals.replace('Max Prime *e','Max Prime').replace('HBO Plus *e','HBO Plus')
		f.write('    <item>\n        <title>''[COLOR lime]|>[/COLOR]'+'[COLOR darkseagreen]%s[/COLOR]'%canals+' [COLOR lime]  < - >  [/COLOR]'' [COLOR white]''[COLOR white]'+name+'[/COLOR]''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR darkseagreen]'+hora+'[/COLOR]''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR white]'+cate+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]''</title>\n        <link>	</link>\n        <thumbnail>	</thumbnail>\n        <fanart>	</fanart>\n        <info>	</info>\n    </item>\n\n')
		addDir('[COLOR lime]\n|>   [/COLOR]'+'[COLOR darkseagreen]%s[/COLOR]'%canals+' [COLOR lime]  < - >  [/COLOR]'' [COLOR white]''[COLOR white]'+name+'[/COLOR]''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR darkseagreen]'+hora+'[/COLOR]''[COLOR lime]  < - >  [/COLOR]''[COLOR white]'' [COLOR white]'+cate+'[/COLOR]'+'[COLOR lime]   <|[/COLOR]',base2+url,96,artfolder + 'icon.png')
	f.write('        </items>\n    </channel>\n</channels>\n\n\n')		
	f.close()	
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin("Container.SetViewMode(51)")	