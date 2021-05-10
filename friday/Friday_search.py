import boss
import time
import requests
import pyttsx3
import datetime
import webbrowser
import Friday_infor
import speech_recognition 
import Friday_conversation

# Friday setting up to say 
friday = pyttsx3.init()
friday_hearing = speech_recognition.Recognizer()
voice = friday.getProperty('voices')
# friday.setProperty('voice',voice[1].id)
rate = friday.getProperty('rate')   
friday.setProperty('rate', 200)    

def speak(audio):
    friday.setProperty('rate', 180)  
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

def Browser(link):
    url=f"{link}"
    webbrowser.get().open(url)

def search(str):
        if "google" in str:
            speak("What should i search Boss")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f'Here is your {search} on google chrome')
        elif "youtube" in str:
            speak("What should i search Boss")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open facebook" in str:
            speak("facebook is opening")  
            Browser('https://www.facebook.com/')
        elif "music" in str:
            speak("Do you want to listen to music")
            speak("opening music on youtube")
            Browser('https://www.youtube.com/watch?v=leAlprToECY&list=PLfauYiLl00OpKReDoJbtrwKRIyOQiFH2a')
        elif "watching film" in str:
            speak("Opening film on browser")
            Browser('http://www.phimmoizz.net')
        elif "game" in str:
            speak("Opening garena")
            Browser('C:/Program Files (x86)/Garena/Garena/Garena.exe')
        elif "photo" in str:
            speak("Opening photo on google chrome")
            Browser('https://photos.google.com')
        elif "where is" in str:
            print(str[9:len(str)])
            location = str[9:len(str)]
            speak(f'Here is {location} on google maps')
            url=f"https://www.google.com/maps/place/{str[9:len(str)]}"
            webbrowser.get().open(url)
        elif "weather" in str:
            try:
                    speak("Tell me about the city:")
                    city = command()
                    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
                    url = api_address + city
                    json_data = requests.get(url).json()
                    format_add_temp = json_data['main']['temp']
                    humidity = json_data['main']['humidity']
                    wind = json_data['wind']['speed']
                    weather_description = json_data['weather'][0]['description'] #drizzle 
                    visibility = json_data['visibility']
                    # print(json_data)
                    speak(f"the temperature of {city} city is {int(format_add_temp - 273)} degrees Celsius")
                    speak(f"the humidity is {humidity} percent")
                    speak(f"wind speed is {wind} meter per second")
                    speak(f"visibility  is {int(visibility/1000)} kilometer")
                    speak(f"The weather is {weather_description}")
                    print(int(format_add_temp - 273))
                    print(humidity)
                    print(wind)
                    print(int(visibility/1000))
                    print(weather_description)
                    try:
                        add_Des = json_data['weather'][1]['main'] #drizzle 
                        speak(f"and {add_Des}")
                        print(add_Des)
                    except:
                        print("No data des add")
            except:
                    try:
                        speak("The city invalid, please try again")
                        speak("Tell me about the city:")
                        city = command()
                        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
                        url = api_address + city
                        json_data = requests.get(url).json()
                        format_add_temp = json_data['main']['temp']
                        humidity = json_data['main']['humidity']
                        wind = json_data['wind']['speed']
                        weather_description = json_data['weather'][0]['description'] #drizzle 
                        visibility = json_data['visibility']
                        # print(json_data)
                        speak(f"the temperature of {city} city is {int(format_add_temp - 273)} degrees Celsius")
                        speak(f"the humidity is {humidity} percent")
                        speak(f"wind speed is {wind} meter per second")
                        speak(f"visibility  is {int(visibility/1000)} kilometer")
                        speak(f"The weather is {weather_description}")
                        print("temp :", int(format_add_temp - 273))
                        print("humandity: ",humidity)
                        print("wind: ", wind)
                        print(int(visibility/1000))
                        print(weather_description)
                        try:
                            add_Des = json_data['weather'][1]['main'] #drizzle 
                            speak(f"and {add_Des}")
                            print(add_Des)
                        except:
                            print("No data des add")
                    except:
                        speak("The city invalid, try later")
          
        elif "search" in str:
            print(str[7:len(str)])
            search = str[7:len(str)]
            speak(f'Here is {search} on google chrome')
            url=f"https://www.google.com/search?q={str[7:len(str)]}"
            webbrowser.get().open(url)


