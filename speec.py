from gtts import gTTS
import pyttsx3
from playsound import playsound
import speec as sp
import os
import time
import speech_recognition as sr #importamos o modúlo


def ouvir():
    rec = sr.Recognizer() #instanciamos o modúlo do reconhecedor

    with sr.Microphone() as fala: #chamos a gravação do microphone de fala
	    frase = rec.listen(fala) #o metodo listen vai ouvir o que a gente falar e gravar na variavel frase

    return rec.recognize_google(frase, language='pt')

def falar(texto):
    en = pyttsx3.init()
    en.setProperty('voice',b'brazil')
    en.say(texto)
    en.runAndWait()