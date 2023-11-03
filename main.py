import requests
import win32com.client as wincom
import json
speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    city = input("enter the name of the city: \n")
    url = f"https://api.weatherapi.com/v1/current.json?key=f5d8aa72a5d54e24bc8162948230211&q={city}"

    r = requests.get(url)
    wdic = json.loads(r.text)

    w = wdic["current"]["temp_c"]
    speak.Speak(f"'the current wheather of {city} is {w} degree")



