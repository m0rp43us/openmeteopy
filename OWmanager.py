"""
A module for downloading meteorological date from the open-meteo API (https://open-meteo.com/en/).
Name: Wail Chalabi
e-mail: wail.agroconcept@gmail.com
Version: 0.0.1
"""


import requests
import json

from requests import exceptions
from Options import *
from Daily import *
from Hourly import *


class OWmanager():

    def __init__(self, options, hourly = None,daily = None):
        
        """
        Entry point class providing ad-hoc API clients for each OW web API.

        Args:
            options (Options): options for the /v1/forecast endpoint .
            hourly (Hourly): Hourly parameter object.
            daily (Daily) : Daily parameter object.
        """

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
    def get_data(self):
        try:
            r  = requests.get(self.url, params = self.payload)
            print(r.status_code)
            if r.status_code != 200 and r.status_code != 400:
                raise BaseException("Failed retrieving open-meteo data, server returned HTTP code: {} on following URL {}.".format(r.status_code, r.url))
            if "reason" in r :
                raise ApiCallError(r)
            return json.loads(r.content.decode('utf-8'))
        except requests.ConnectionError as e :
            raise(e)

hourly = Hourly()
daily = Daily()
options = Options(52.52,13.41)

mgr = OWmanager(options,
    hourly.all(),
    daily.all())

print(mgr.get_data())
