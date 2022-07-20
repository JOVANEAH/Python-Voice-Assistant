import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def playmusic(query):
    musicdir = ['C:\\Users\\Jovan\\Music\\JWLibrary\\jw1.mp3', 'C:\\Users\\Jovan\\Music\\JWLibrary\\jw2.mp3','C:\\Users\\Jovan\\Music\\JWLibrary\\jw3.mp3','C:\\Users\\Jovan\\Music\\JWLibrary\\jw4.mp3','C:\\Users\\Jovan\\Music\\JWLibrary\\jw5.mp3','C:\\Users\\Jovan\\Music\\JWLibrary\\jw6.mp3','C:\\Users\\Jovan\\Music\\JWLibrary\\jw7.mp3','C:\\Users\\Jovan\\Music\\JWLibrary\\jw8.mp3']
    speak("enjoy it!")
    os.startfile(os.path.join(random.choice(musicdir)))

def tired(query):
    tireddir = ['C:\\Users\\Jovan\\Music\\song\\tujuhbelas1.mp3','C:\\Users\\Jovan\\Music\\song\\catatankecil.mp3','C:\\Users\\Jovan\\Music\\song\\lebihindah.mp3','C:\\Users\\Jovan\\Music\\song\\lemontree.mp3','C:\\Users\\Jovan\\Music\\song\\photograph.m4a','C:\\Users\\Jovan\\Music\\song\\menghapusjejakmu.mp3']
    speak("Enjoy this, bro!")
    os.startfile(os.path.join(random.choice(tireddir)))