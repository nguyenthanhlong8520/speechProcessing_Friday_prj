import speech_recognition 
import pyttsx3
import datetime
import webbrowser
import Friday_infor
import Friday_conversation
import boss
import ctypes
import time

# Friday setting up to say 
friday = pyttsx3.init()
# voice = friday.getProperty('voices')
# friday.setProperty('voice',voice[1].id)
friday_hearing = speech_recognition.Recognizer()
rate = friday.getProperty('rate')   
friday.setProperty('rate', 150)             

def speak(audio):
    friday.say(audio)
    friday.runAndWait()

def command():
    with speech_recognition.Microphone() as mic:
        audio = friday_hearing.record(mic, duration = 3)
    try:
        voice_boss = friday_hearing.recognize_google(audio, language='en')
        print(voice_boss)
    except speech_recognition.UnknownValueError:
        voice_boss = ""
        print("...")
    return voice_boss

def time_():
    friday.setProperty('rate', 160)     
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    friday.say(f"The time is {Time}")
    friday.setProperty('rate', 200) 
    friday.runAndWait()
    print(Time)

def praise():   
    friday.setProperty('rate', 160)     
    friday.say("oh boss, thanks")
    friday.setProperty('rate', 200) 
    friday.runAndWait()

def conversation(str):
        if "hello" in str:
            speak("hello my boss, how can i help you")   
        elif 'how are you' in str:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'i am fine' in str or "crazy" in str:
            speak("It's good to know that your fine")
        elif "time" in str:
            time_()
        elif "hi friday" in str:
            speak("I'm listening")   
        elif "your name" in str:
            Friday_infor.Name()
        elif "myself" in str:
            boss.infor_boss()
        elif "contact" in str:
            boss.contact()
        elif "very good" in str:
            Friday_conversation.praise()
        elif 'window' in str:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        elif "don't listen" in str or "stop listening" in str:
            speak("for how much time you want to stop FRIDAY from listening commands")
            try:
                a = int(command())
                speak(f'time to slepp is {a} second')
                time.sleep(a)
                speak("Hello boss, I'm waiting for command")
            except:
                try:    
                    speak("please try again")
                    a = int(command())
                    speak(f'time to slepp is {a} second')
                    time.sleep(a)
                    speak("Hello boss, I'm waiting for command")
                except:
                    speak("Exception for set up the time, try later")
        elif "write a note" in str:
            speak("What should i write, sir")
            note = command()
            file = open('C:/Users/nguye/OneDrive/Máy tính/jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%I:%M:%p")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            speak("write success")
        elif "show note" in str:
            speak("Showing Notes")
            file = open("C:/Users/nguye/OneDrive/Máy tính/jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))
        elif "goodbye" in str:
            speak("Have a nice day boss, goodbye")
            quit()

def openFriday():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour <= 10:
        speak("Good morning, Boss")
    elif hour >= 11 and hour <= 12:
        speak("Good noon, Boss")
    elif hour >= 13 and hour <= 18:
        speak("Good afternoon, Boss")
    elif hour >= 19 and hour <= 21:
        speak("Good evening, Boss")
    else:
        speak("Good night, Boss")
    speak("How can i help you")

