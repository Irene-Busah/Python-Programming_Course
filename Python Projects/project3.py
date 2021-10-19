import requests

# Getting weather information

from pprint import pprint

API_Key = "4706a144e8220c712887fb70e080f2a8"
city = input('Enter a city: ')

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)
