"""
A module for downloading meteorological data from the open-meteo API (https://open-meteo.com/en/).
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
    """OpenMeteo class is the client to manage http to Open-Meteo public APIs requests.add

    """
    def __init__(self, options: Option, hourly = None, daily = None, fifteen_minutes = None, api_key = None):
        """
        Args:
            options:
            provides:
            hourly:
            dailt:
            fifteen_minutes:
            api_key:
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
            res = requests.get(self.url, params=self.payload)
            if res.status_code != 200 and res.status_code != 400:
                raise BaseException("Failed retrieving open-meteo data, server returned HTTP code: {} on following URL {}.".format(res.status_code, res.url))
            elif "reason" in res:
                raise ApiCallError(res)
            else:
                return res.json()
        except requests.ConnectionError as e:
            raise(e)
        
    # TODO: get_dict()
    def get_dict(self) -> dict:
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
        
        return cleaned_data
    
    # TODO: get_json_str()
    def get_json_str(self) -> str:
        """Return the dict object as a json string format.

        Returns:
            str: a string containing the cleaned response from the Open-Meteo APIs in JSON format.
        """
        return json.dumps(self.get_dict())
    
    # TODO: get_numpy()
    def get_numpy(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return

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
    #       specify that the string for filepath must have .csv at the end
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
    def save_excel(self, filepath: str):
        """_summary_

        Args:
            filepath (str): _description_

        Returns:
            _type_: _description_
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

    # TODO: save_json()
    #       specify that the string for the filepath should have .json at the end 
    def save_json(self, filepath:str):
        # Write the Python object to a JSON file
        data = self.get_dict
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file)