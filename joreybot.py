from click import command
import pyaudio
from base64 import encode
from datetime import datetime
from email.mime import audio
from re import search
from grpc import server
import pyttsx3
from requests import request
import speech_recognition as sr
import datetime
from playsound import playsound
import wikipedia
import webbrowser
import os
import smtplib
import random
import json
import pyjokes
import pywhatkit

file_json = open("data.json")
data = json.loads(file_json.read())


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jorey-bot, Please tell me how may I help you")


def takeCommand():
    #Take microphone input and return it as a string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print("User said: " + query +"\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:  
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            engine.setProperty('rate', 150)
            speak(results)
            engine.setProperty('rate', 200)            
        elif 'website' in query:
            speak("Here you go!")
            webbrowser.open("https://jovaneah.github.io/")
        elif 'search in google' in query:
            speak("What do you want me to search?")
            searching = takeCommand()
            speak("Searching "+searching)
            webbrowser.open('https://www.google.com/search?client=firefox-b-d&q='+searching)
        elif 'search in youtube' in query:
            speak("What do you want me to search?")
            youtube = takeCommand()
            speak("Okay! here you go!")
            webbrowser.open('https://www.youtube.com/results?search_query='+youtube)
        elif 'play music' in query:
            from Musicdir import playmusic
            playmusic(query)
        elif 'play song' in query:
            from Musicdir import tired
            tired(query)
        elif 'the time' in query:
            word = ['The time is ', 'it\'s ']
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            engine.setProperty('rate', 150)
            speak(random.choice(word)+strTime)
        elif 'thank you' in query:
            thank = ['Your welcome', 'No problem', 'My pleasure']
            speak(random.choice(thank))
        elif 'open' in query:
            from Dictapp import openappweb
            openappweb(query)
        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)
        elif 'sorry' in query:
            speak("It's okay")
        elif 'happy' in query:
            speak("I'm glad to hear that!")
        elif 'hello' in query:
            speak("Hello!")
        elif 'how are you' in query:
            speak("Fine as usual!")
            speak("And you?")
            inpt = takeCommand()
            if 'fine' in inpt:
                speak("Nice!")
            elif 'tired' in inpt:
                from Musicdir import playmusic
                playmusic(query)
            elif 'bad' in inpt:
                from Musicdir import tired
                tired(query)
        elif 'what are you doing' in query:
            speak("I'm learning your code!")
        elif 'yo' in query:
            speak("Yo")
        elif 'test' in query:
            speak("Hello, hello. I can hear you!")
        elif "whatsapp" in query:
            from Whatsapp import sendMessage
            sendMessage()
        elif "go to sleep" in query:
            speak("Going to sleep")
            exit()
