"""
A module for downloading meteorological data from the open-meteo API (https://open-meteo.com/en/).
Name: Wail Chalabi
e-mail: wailchalabi1996@gmail.com
Version: 1.0.0
"""

import http.client
import requests
import json
import pandas as pd
import numpy as np
from openmeteopy import ApiCallError,FilepathNotFilled,FileOptionError
from enum import Enum


_providers = { 
    "gem" : "https://api.open-meteo.com/v1/gem?",
    "metno" : "https://api.open-meteo.com/v1/metno?",
    "jma" : "https://api.open-meteo.com/v1/jma?",
    "dwd_icon" : "https://api.open-meteo.com/v1/dwd-icon?",
    "meteofrance" : "https://api.open-meteo.com/v1/meteofrance?",
    "gfs" : "https://api.open-meteo.com/v1/gfs?",
    "ecmwf" : "https://api.open-meteo.com/v1/ecmwf?",
    "historical" : "https://archive-api.open-meteo.com/v1/archive?",
    "marine" : "https://marine-api.open-meteo.com/v1/marine?",
    "air_quality" : "https://air-quality-api.open-meteo.com/v1/air-quality?",
    "geocoding" : "https://geocoding-api.open-meteo.com/v1/search?",
    "elevation" : "https://api.open-meteo.com/v1/elevation?",
    "flood" : "https://flood-api.open-meteo.com/v1/flood?",
    "forecast" : "https://api.open-meteo.com/v1/forecast?",
}

class OpenMeteo():   
    """OpenMeteo class is the client to manage http to Open-Meteo public APIs requests.add

    """
    def __init__(self, options, provider:str = None, hourly = None, daily = None, fifteen_minutes = None, api_key = None):
        """
        Args:
            options:
            provides:
            hourly:
            dailt:
            fifteen_minutes:
            api_key:
        """ 
        #self.payload = {}
        self.options = options
        self.hourly = hourly
        self.daily = daily
        self.fifteen_minutes = fifteen_minutes
        
        if provider not in list(_providers.keys()):
            raise BaseException('Invalid provider, please check the openmeteopy documentation for the valid providers.')
        else:
            self.url = _providers[provider]
            if provider == "geocoding" :
                self.payload = {
                    "name": options.name,
                    "count": options.count,
                    "format": options.format,
                    "language" : options.language
                    }
            elif provider == "elevation":
                self.payload = {
                    "latitude": options.latitude,
                    "longitude": options.longitude
                    }
            elif provider == "marine":
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
            elif provider == "gem":
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
            elif provider == "metno":
                if options.start_end :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "timezone": options.timezone,
                        "windspeed_unit":options.windspeed_unit,
                        "precipitation_unit":options.precipitation_unit,
                        "timeformat":options.timeformat,
                        "current_weather":options.current_weather,
                        "past_days":options.past_days,
                        "self.temperature_unit" : options.temperature_unit,
                        "start_date" : options.start_date ,
                        "end_date": options.end_date,
                        "cell_selection" : options.cell_selection
                        }
                else :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "timezone": options.timezone,
                        "windspeed_unit":options.windspeed_unit,
                        "precipitation_unit":options.precipitation_unit,
                        "timeformat":options.timeformat,
                        "current_weather":options.current_weather,
                        "past_days":options.past_days,
                        "self.temperature_unit" : options.temperature_unit,
                        "cell_selection" : options.cell_selection
                        }
            elif provider == "flood":
                if options.start_end :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "timeformat":options.timeformat,
                        "past_days":options.past_days,
                        "forecast_days" : options.forecast_days,
                        "start_date" : options.start_date ,
                        "end_date": options.end_date,
                        "ensemble" : options.ensemble,
                        "cell_selection" : options.cell_selection
                        }
                else :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "timeformat":options.timeformat,
                        "past_days":options.past_days,
                        "forecast_days" : options.forecast_days,
                        "ensemble" : options.ensemble,
                        "cell_selection" : options.cell_selection
                        }
            elif provider == "meteofrance" or provider == "jma" or provider == "dwd_icon" :
                if options.start_end :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "elevation" : options.elevation,
                        "timezone": options.timezone,
                        "timeformat":options.timeformat,
                        "past_days":options.past_days,
                        "temperature_unit" : options.temperature_unit,
                        "current_weather":options.current_weather,
                        "windspeed_unit" : options.windspeed_unit,
                        "precipitation_unit": options.precipitation_unit,
                        "start_date" : options.start_date ,
                        "end_date": options.end_date,
                        "cell_selection" : options.cell_selection
                        }
                else :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "elevation" : options.elevation,
                        "timeformat":options.timeformat,
                        "timezone": options.timezone,
                        "past_days":options.past_days,
                        "temperature_unit" : options.temperature_unit,
                        "current_weather":options.current_weather,
                        "windspeed_unit" : options.windspeed_unit,
                        "precipitation_unit": options.precipitation_unit,
                        "cell_selection" : options.cell_selection
                        }
            elif provider == "ecmwf":
                if options.start_end :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "elevation" : options.elevation,
                        "timeformat":options.timeformat,
                        "past_days":options.past_days,
                        "temperature_unit" : options.temperature_unit,
                        "current_weather":options.current_weather,
                        "windspeed_unit" : options.windspeed_unit,
                        "precipitation_unit": options.precipitation_unit,
                        "start_date" : options.start_date ,
                        "end_date": options.end_date,
                        "cell_selection" : options.cell_selection
                        }
                else :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "elevation" : options.elevation,
                        "timeformat":options.timeformat,
                        "past_days":options.past_days,
                        "temperature_unit" : options.temperature_unit,
                        "current_weather":options.current_weather,
                        "windspeed_unit" : options.windspeed_unit,
                        "precipitation_unit": options.precipitation_unit,
                        "cell_selection" : options.cell_selection,
                        "forecast_days" : options.forecast_days
                        }
            elif provider == "forecast":
                self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "timezone": options.timezone,
                        "windspeed_unit":options.windspeed_unit,
                        "precipitation_unit":options.precipitation_unit,
                        "timeformat":options.timeformat,
                        "past_days":options.past_days
                        }
            elif provider == "gfs":
                if options.start_end :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "elevation" : options.elevation,
                        "timezone": options.timezone,
                        "timeformat":options.timeformat,
                        "past_days":options.past_days,
                        "temperature_unit" : options.temperature_unit,
                        "current_weather":options.current_weather,
                        "windspeed_unit" : options.windspeed_unit,
                        "precipitation_unit": options.precipitation_unit,
                        "forecast_days":options.forecast_days,
                        "start_date" : options.start_date ,
                        "end_date": options.end_date,
                        "cell_selection" : options.cell_selection
                        }
                else :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "elevation" : options.elevation,
                        "timeformat":options.timeformat,
                        "timezone": options.timezone,
                        "past_days":options.past_days,
                        "temperature_unit" : options.temperature_unit,
                        "current_weather":options.current_weather,
                        "windspeed_unit" : options.windspeed_unit,
                        "precipitation_unit": options.precipitation_unit,
                        "forecast_days":options.forecast_days,
                        "cell_selection" : options.cell_selection
                        }
            elif provider == "historical":
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "elevation" : options.elevation,
                        "timezone": options.timezone,
                        "timeformat":options.timeformat,
                        "temperature_unit" : options.temperature_unit,
                        "current_weather":options.current_weather,
                        "windspeed_unit" : options.windspeed_unit,
                        "precipitation_unit": options.precipitation_unit,
                        "start_date" : options.start_date ,
                        "end_date": options.end_date,
                        "cell_selection" : options.cell_selection
                        }
            elif provider == "air_quality":
                if options.start_end :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "domains" : options.domains,
                        "timezone": options.timezone,
                        "timeformat":options.timeformat,
                        "past_days":options.past_days,
                        "start_date" : options.start_date ,
                        "end_date": options.end_date,
                        "cell_selection" : options.cell_selection
                        }
                else :
                    self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "domains" : options.domains,
                        "timeformat":options.timeformat,
                        "timezone": options.timezone,
                        "past_days":options.past_days,
                        "cell_selection" : options.cell_selection
                        }
        if self.daily != None :
            self.payload['daily'] = ','.join(self.daily.daily_params)
        if self.hourly != None :
            self.payload['hourly'] = ','.join(self.hourly.hourly_params)
        if self.fifteen_minutes != None :
            self.payload['minutely_15'] = ','.join(self.fifteen_minutes.minutes_15_params)
        if api_key != None:
            self.payload['apikey'] = api_key
            self.url = "https://customer-api.open-meteo.com/v1/forecast?"
        self.payload = "&".join("%s=%s" % (k,v) for k,v in self.payload.items())


    # TODO: Complete this function as an explicit version of the get_data function
    #       Delete int values to select options for resonses data type
    def _fetch(self):
        """Calls Open-Meteo API with the payload saved in this class and return original json

        Raises:
            :BaseException: HTTP error
            :ApiCallError: Api resonse error
            :ConnectionError: requests connection error (internet connection or server having some trouble)
        Returns:
            :json: response from the dataset in json
        """
        try:
            res = requests.get(self.url, params = self.payload)
            if res.status_code != 200 and res.status_code != 400:
                raise BaseException("Failed retrieving open-meteo data, server returned HTTP code: {} on following URL {}.".format(res.status_code, res.url))
            elif "reason" in res:
                raise ApiCallError(res)
            else:
                return res.json()
        except requests.ConnectionError as e:
            raise(e)
        
    # TODO: get_json()
    def get_json(self) -> str:
        """Retrieve a json object from the open-meteo APIs.

        Returns:
            str: A "cleaned" version of the server response in JSON format as a string. It only includes hourly, daily or minutely_15 attributes.
        """
        res = self._fetch()
        cleaned_data = {}
        if "hourly" in res and "daily" in res:
            cleaned_data["hourly"] = res["hourly"]
            cleaned_data["daily"] = res["daily"]
        elif "hourly" in res and "daily" not in res:
            cleaned_data["hourly"] = res["hourly"]
        elif "hourly" not in res and "daily" in res :
            cleaned_data["daily"] = res["daily"]
        else :
            cleaned_data = res
        if "minutely_15" in res:
            cleaned_data["minutely_15"] = res["minutely_15"]
        
        return json.dumps(cleaned_data)
    
    # TODO: get_numpy()

    # TODO: get_pandas()
    def get_pandas(self) -> pd.DataFrame:
        """This function builds a pandas dataframe from the open-meteo APIs responses.

        Returns:
            DataFrame: pandas dataframe with time as index and each of the columns is one of the attribute requested.
        """
        res = self._fetch()

        if "hourly" in res and "daily" in res:
            df_hourly = pd.DataFrame(res['hourly'])
            df_daily = pd.DataFrame(res['daily'])
            df_hourly = df_hourly.set_index('time')
            df_daily = df_daily.set_index('time')
            return df_hourly, df_daily
        elif "hourly" in res and "daily" not in res:
            df_hourly = pd.DataFrame(res['hourly'])
            df_hourly = df_hourly.set_index('time')
            return df_hourly
        elif "hourly" not in res and "daily" in res :
            df_daily = pd.DataFrame(res['daily'])
            df_daily = df_daily.set_index('time')
            return df_daily
        elif "minutely_15" in res:
            df_minutely = pd.DataFrame(res['minutely_15'])
            df_minutely = df_minutely.set_index('time')
            return df_minutely
        else :
            return None


    # TODO: save_csv()
    def save_csv(self, filepath: str):
        """This function directly save the content of response from open-meteo APIs into a csv file

        Returns:
            DataFrame: pandas dataframe with time as index and each of the columns is one of the attribute requested.
        """
        df = self.get_pandas()

        # if self.hourly != None and self.daily == None and self.fifteen_minutes == None:
        #     df.to_csv(filepath)
        # elif self.hourly == None and self.daily == None and self.fifteen_minutes == None:
        #     df.to_csv(filepath)
        # elif self.hourly != None and self.daily == None and self.fifteen_minutes == None:
        #     df.to_csv(filepath)
        df.to_csv(filepath+'.csv')

        return df
        
    # TODO: save_excel()