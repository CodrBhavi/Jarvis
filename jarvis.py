from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from tkinter import *
import webbrowser
from pytube import YouTube
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0])

def speak(audio):
    # This Speak Function helps Jarvis to Speak
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty("rate", 178)

def wishMe():
    # This Function will greet you according to Time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
def takeCommand():
    # It takes Microphone Input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing........")
        query = r.recognize_google(audio,language = "en-IN")
        print("User Said: ",query)
    except Exception as e:
        # print(e)
        print("Say that Again Please.......")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    speak("I am Jarvis your Assistant How may I help you?")
    # Logic for executing tasks based on query
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia........")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            speak("For more Information Visit Wikipedia")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music = "F:\Music"
            songs = os.listdir(music)
            speak("Playing Music")
            os.startfile(os.path.join(music,songs[0]))