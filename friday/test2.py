import ctypes
import time
import keyboard
# dll = ctypes.WinDLL('user32.dll')
# dll.LockWorkStation()
# time.sleep(2)
# keyboard.send('enter')
# keyboard.send('l,o,n,g,8,5,2,0')
# keyboard.send('enter')


# elif "write a note" in query:
#             speak("What should i write, sir")
#             note = takeCommand()
#             file = open('jarvis.txt', 'w')
#             speak("Sir, Should i include date and time")
#             snfm = takeCommand()
#             if 'yes' in snfm or 'sure' in snfm:
#                 strTime = datetime.datetime.now().strftime("% H:% M:% S")
#                 file.write(strTime)
#                 file.write(" :- ")
#                 file.write(note)
#             else:
#                 file.write(note)
         
#         elif "show note" in query:
#             speak("Showing Notes")
#             file = open("jarvis.txt", "r") 
#             print(file.read())
#             speak(file.read(6))

import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()

weather_description = json_data['weather'][0]['description'] #drizzle 
visibility = json_data['visibility']
try :
    add_Des = json_data['weather'][1]['main'] #drizzle 
    print(add_Des)
except:
    pass

print(json_data)
print(weather_description)
print(visibility)
