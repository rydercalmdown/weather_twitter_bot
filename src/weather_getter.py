import os
import logging
import requests


class WeatherGetter():
    """Class for retrieving the weather"""

    def __init__(self):
        """Set up the class"""
        self.city = 'toronto'

    def _get_weather_api_key(self):
        """Returns the weather API key"""
        return os.environ['WEATHER_API_KEY']

    def _get_weather_from_api(self):
        """Returns the response from the weather api"""
        logging.info('Retrieving weather from API')
        proto = 'https'
        host = 'api.openweathermap.org'
        endpoint = '/data/2.5/weather'
        params = {
            'q': self.city,
            'appid': self._get_weather_api_key(),
        }
        url = proto + '://' + host + endpoint
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()

    def _get_temp(self):
        """Returns the temperature"""
        return round(int(self.wx['main']['temp']) - 273.15)

    def _get_weather_desc(self):
        """Returns a description of the weather"""
        return self.wx['weather'][0]['description']

    def get_weather(self):
        """Gets the weather from remote and sets class properties"""
        self.wx = self._get_weather_from_api()
        logging.debug(self.wx)
        self.description = self._get_weather_desc()
        self.temp = self._get_temp()
        logging.debug(self.temp)
