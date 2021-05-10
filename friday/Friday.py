import speech_recognition 
import pyttsx3
import datetime
import webbrowser
import Friday_infor
import Friday_conversation
import Friday_search
import boss

# Friday setting up to say 
friday = pyttsx3.init()
friday_hearing = speech_recognition.Recognizer()
# voice = friday.getProperty('voices')
# friday.setProperty('voice',voice[1].id)

def speak(audio):
    friday.setProperty('rate', 160)     
    friday.say(audio)
    friday.setProperty('rate', 200) 
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    # friday.say("it")
    speak(f"The time is {Time}")
    # speak(Time)
    print(Time)

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


if __name__ == "__main__":
    Friday_conversation.openFriday()
    while True:
        voice_boss = command().lower()
        Friday_search.search(voice_boss)
        Friday_conversation.conversation(voice_boss)