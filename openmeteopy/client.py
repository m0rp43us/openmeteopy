"""
A module for downloading meteorological data from the Open-Meteo APIs (https://open-meteo.com/en/).
Name: Wail Chalabi
e-mail: wailchalabi1996@gmail.com
Version: 1.0.0
"""

import requests
import json
import pandas as pd
import numpy as np
from openmeteopy import ApiCallError,FilepathNotFilled,FileOptionError
from .options.option import Option
from .options import *

class OpenMeteo():   
    """OpenMeteo class is the client to manage http to Open-Meteo public APIs requests.

    """
    def __init__(self, options: Option, hourly = None, daily = None, fifteen_minutes = None, api_key = None):
        """
        Args:
            options: This paramete is a Option object that specify the provider, geocoordinates and time period to fetch data.
            hourly: This parameter is a Hourly object that specify the meteorological variables required with hourly frequency.
            daily: This parameter is a Daily object that specify the meteorological variables required with daily frequency.
            fifteen_minutes: This parameter is a FifteenMinutes object that specify the meteorological variables required with fifteen minutes frequency.
            api_key: This parameter specify a private API key for commercial use.
        """ 
        self.options = options
        self.hourly = hourly
        self.daily = daily
        self.fifteen_minutes = fifteen_minutes
        
        self.url = options.get_api_path()
        self.payload = options.get_payload()
        
        if self.daily != None:
            self.payload['daily'] = ','.join(self.daily.daily_params)
        if self.hourly != None:
            self.payload['hourly'] = ','.join(self.hourly.hourly_params)
        if self.fifteen_minutes != None:
            self.payload['minutely_15'] = ','.join(self.fifteen_minutes.minutes_15_params)
        if api_key != None:
            self.payload['apikey'] = api_key
            self.url = "https://customer-api.open-meteo.com/v1/forecast?"
        self.payload = "&".join("%s=%s" % (k,v) for k,v in self.payload.items())


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
            res = requests.get(self.url, params=self.payload)
            if res.status_code != 200 and res.status_code != 400:
                raise BaseException("Failed retrieving open-meteo data, server returned HTTP code: {} on following URL {}.".format(res.status_code, res.url))
            elif "reason" in res:
                raise ApiCallError(res)
            else:
                return res
        except requests.ConnectionError as e:
            raise(e)
        
    def get_dict(self) -> dict:
        """Get the response from Open-Meteo API as a python dictionary.

        Returns:
            dict: A "cleaned" version of the server response returned as a python dictionary. It only includes hourly, daily or minutely_15 attributes.
        """
        res = self._fetch().json()
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
        
        return cleaned_data
    
    def get_json_str(self) -> str:
        """Get the response from Open-Meteo API as a string in JSON format.

        Returns:
            str: a string containing the cleaned response from the Open-Meteo APIs in JSON format.
        """
        return json.dumps(self.get_dict())
    
    def get_pandas(self) -> pd.DataFrame:
        """Get the response from Open-Meteo API as a pandas DataFrame format.

        Returns:
            DataFrame: pandas dataframe with time as index and each of the columns is one of the attribute required.
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

    # TODO: get_numpy()
    def get_numpy(self) -> np.ndarray:
        """Get the response from Open-Meteo API as a numpy array.

        Returns:
            np.ndarray: a numpy array with shape (N, M), where N is the number of hourly/daily/fifteen_minutes samples and M is the number of meteorological variables required 
        """
        df = self.get_pandas()
        arr = df.to_numpy()
        return arr
    
    def save_csv(self, filepath: str):
        """This function directly save the content of response from open-meteo APIs into a csv file

        Args:
            filepath (str): filepath where the .csv file will be saved.

        Returns:
            DataFrame: pandas dataframe with time as index and each of the columns is one of the attribute requested.
        """

        df = self.get_pandas()
        df.to_csv(filepath+'.csv')

        return df
        
    def save_excel(self, filepath: str):
        """This function directly save the content of response from open-meteo APIs into a excel file

        Args:
            filepath (str): filepath where the .excel file will be saved.

        Returns:
            DataFrame: pandas dataframe with time as index and each of the columns is one of the attribute requested.
        """

        df = self.get_pandas()
        df.to_excel(filepath+'.excel')

        return df

    def save_json(self, filepath:str):
        """_summary_

        Args:
            filepath (str): filepath where the .json file will be saved.
        """

        data = self.get_dict()
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file)