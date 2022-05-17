import requests
from pprint import pprint

API_Key = 'b960e657d88a137a88622a486f8bd92c'

city = input('Enter a City: ')
base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_Key + '&q=' + city

weather_data = requests.get(base_url).json()

pprint(weather_data)

