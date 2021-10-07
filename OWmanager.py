import requests

from Options import *
from Daily import *
from Hourly import *


class OWmanager():

    def __init__(self, options, hourly = None,daily = None):
        
        self.options = options
        self.hourly = hourly
        self.daily = daily
        self.url = "https://api.open-meteo.com/v1/forecast?"
        self.payload = {
            "latitude": options.latitude,
            "longitude": options.longitude,
            "timezone": options.timezone,
            "windspeed_unit":options.windspeed_unit,
            "precipitation_unit":options.precipitation_unit,
            "timeformat":options.timeformat,
            "current_weather":options.current_weather,
            "past_days":options.past_days
            }
        if self.daily != None :
            self.payload['daily'] = ','.join(self.daily.daily_params)
        if self.hourly != None :
            self.payload['hourly'] = ','.join(self.hourly.hourly_params)
        self.payload = "&".join("%s=%s" % (k,v) for k,v in self.payload.items())

    options = Options(52.52,13.41)
    def get_data(self):
        print(requests.get(self.url, params = self.payload).content)
        print(requests.get(self.url, params = self.payload).url)

hourly = Hourly()
daily = Daily()


mgr = OWmanager(Options(52.52,13.41),
    hourly.all(),
    daily.all())


mgr.get_data()

print(hourly.hourly_params)