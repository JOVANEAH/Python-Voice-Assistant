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
    musicdir = ['C:\\Users\\Jovaneah\\Music\\JWLibrary\\jw1.mp3']
    speak("enjoy it!")
    os.startfile(os.path.join(random.choice(musicdir)))
