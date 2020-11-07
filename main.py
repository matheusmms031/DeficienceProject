import pyttsx3 # importamos o modúlo
import speec as sp
import menu as mn
import os
import time
import search as sc
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr #importamos o modúlo


while True:
	os.system('cls || clear')
	menu = mn.menu(3)
	print(menu)
	sp.falar("teste")
	command = int(input('[x]> '))
	if command == 1:
		while True:
			os.system('cls || clear')
			menu = mn.menu(4)
			print(menu)
			print("Olá digite 1 para começar a gravar sua voz, ou 2 para eu repetir")
			command = int(input('[x]> '))
			if command == 1:
				palavra_chave = sp.ouvir()
				sp.falar(f"Estes foram os resultados encontrados sobre {palavra_chave}")
				results = sc.search(palavra_chave)
				for result in results:
					print(f"""
	Número: {results.index(result)+1}
	Título: {result['Title']}

	Link: {result['Link']}

	Sobre: {result['Content']}
	""")
				sp.falar("Tecle o numero de 0 o mais recomendado há 9 o menos recomendado e verá o resultado da pesquisa,")
				while True:
					command = str(input('[x]> '))
					if command == str(99):
						os.system('cls || clear')
						break
					for count in range(0,len(results)):
						if command == str(count):
							sp.falar(f"Título da Página. {results[count]['Title']}")
							sp.falar(f"Resumo do contéudo. {results[count]['Content']}")
						if command == str(count)+str(1):
							informacoes = sc.wikipedia(results[count]['Link'])
							sp.falar(f"Titulo da página. {informacoes['title']}")
							sp.falar(f"Conteudo Principal. {informacoes['content']}")

			if command == 99:
				break