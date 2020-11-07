import pyttsx3 # importamos o modúlo
import speec as sp
from bs4 import BeautifulSoup
import time
import requests
from apiclient.discovery import build
import speech_recognition as sr #importamos o modúlo

my_api_key = "AIzaSyCEdUAeAotFGkgHG81MMeSPCKHgqddHPEE"
my_cse_id = "1a4228e60bfe99117"
resource = build("customsearch", "v1", developerKey=my_api_key).cse()
list_results = []
def search(data):
    result = resource.list(q=data,cx="1a4228e60bfe99117").execute()
    for item in result['items']:
        list_results.append({'Title':item['title'],'Link':item['link'],'Content':item['snippet']})
    return list_results
        
def wikipedia(link):
    info = {}
    resposta = requests.get(link)
    soup = BeautifulSoup(resposta.content, "html.parser")
    p = soup.find_all('p')
    h1 = soup.find('h1')
    info['title'] = h1.text
    info['content'] = str(p[0].text) + str(p[1].text)
    return info

# print(wikipedia('https://pt.wikipedia.org/wiki/Python'))