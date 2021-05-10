import speech_recognition 
import pyttsx3
import datetime

# Friday setting up to say 
friday = pyttsx3.init()
voice = friday.getProperty('voices')
# friday.setProperty('voice',voice[1].id)
rate = friday.getProperty('rate')   
friday.setProperty('rate', 200)     

def speak(audio):
    friday.setProperty('rate', 180)  
    friday.say(audio)
    friday.runAndWait()

def Name():   
    speak("i'm Friday")



