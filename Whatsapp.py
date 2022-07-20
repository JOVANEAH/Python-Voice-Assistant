import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message")
    a = str(input("Enter the name: "))
    if a == "Reynard" or a == "reynard":
        speak("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+6281296930090",message,time_hour=strTime,time_min=update)
    if a == "Papah" or a == "papah":
        speak("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+628122001625",message,time_hour=strTime,time_min=update)
    if a == "Mamah" or a == "mamah":
        speak("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+628122001631",message,time_hour=strTime,time_min=update)
    if a == "Nathan" or a == "nathan":
        speak("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+6281317046945",message,time_hour=strTime,time_min=update)
    if a == "Natan" or a == "natan":
        speak("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+6287780149591",message,time_hour=strTime,time_min=update)
    if a == "Nethen" or a == "neten":
        speak("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+6281903322552",message,time_hour=strTime,time_min=update)
    if a == "Romi" or a == "romi":
        speak("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+6289638023602",message,time_hour=strTime,time_min=update)