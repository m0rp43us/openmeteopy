import requests

from Options import *


class OWmanager():

    def __init__(self, options, hourly = None,daily = None):
        
        self.options = options
        self.hourly = hourly
        self.daily = daily
        self.url = "https://api.open-meteo.com/v1/forecast?"
        self.payload = {
            "latitude": options.latitude,
            "longitude": options.longitude,
            "hourly": "temperature_2m",
            "daily": 'weathercode',
            "timezone": options.timezone,
            "windspeed_unit":options.windspeed_unit,
            "precipitation_unit":options.precipitation_unit,
            "timeformat":options.timeformat,
            "current_weather":options.current_weather,
            "past_days":options.past_days
            }  if hourly != None and daily != None else ({
            "latitude": options.latitude,
            "longitude": options.longitude,
            "daily": 'weathercode',
            "timezone": options.timezone,
            "windspeed_unit":options.windspeed_unit,
            "precipitation_unit":options.precipitation_unit,
            "timeformat":options.timeformat,
            "current_weather":options.current_weather,
            "past_days":options.past_days
            } if daily != None and hourly == None else ({
            "latitude": options.latitude,
            "longitude": options.longitude,
            "hourly": "temperature_2m",
            "timezone": options.timezone,
            "windspeed_unit":options.windspeed_unit,
            "precipitation_unit":options.precipitation_unit,
            "timeformat":options.timeformat,
            "current_weather":options.current_weather,
            "past_days":options.past_days
            }) if hourly != None and daily == None else ({
            "latitude": options.latitude,
            "longitude": options.longitude,
            "timezone": options.timezone,
            "windspeed_unit":options.windspeed_unit,
            "precipitation_unit":options.precipitation_unit,
            "timeformat":options.timeformat,
            "current_weather":options.current_weather,
            "past_days":options.past_days
            }))
    options = Options(52.52,13.41)
    def get_data(self):
        print(requests.get(self.url, params = self.payload).content)


mgr = OWmanager(Options(52.52,13.41))
mgr.get_data()

