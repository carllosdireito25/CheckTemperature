import os
from pip._vendor import requests
from core.utils.convert_to_celsius import get_celsius_format



class WeatherAPI():
    def __init__(self,):
        self.key = os.environ.get('key_openweather')
        self.url = os.environ.get('main_url_openweather')

    def get_city_temperature(self,city):
        url = f'{self.url}{city}&appid={self.key}'
        data = requests.get(url).json()
        celsius_ret = round(get_celsius_format(data.get('main').get('temp')),2)
        return celsius_ret