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
from openmeteo_py import ApiCallError,FilepathNotFilled,FileOptionError
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

def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except http.client.IncompleteRead as e:
            return e.partial
    return inner

http.client.HTTPResponse.read = patch_http_response_read(http.client.HTTPResponse.read)

class OpenMeteo():   
    def __init__(self, options, provider:str = None, hourly = None, daily = None, fifteen_minutes = None, api_key = None):
         
        """
        Entry point class providing ad-hoc API clients for each OW web API.

        Args:
            options (options) : options for the /v1/forecast endpoint .
            hourly (hourly) : hourly parameter object.
            daily (daily) : daily parameter object.
            api_key (string) : commercial API key.
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

    # # TODO: Check if this function correctly return a pandas df
    # def dataframit(self, meteo, format = 0, filepath = None):
    #     """Returns a dataframe with each variable having keys as dates,result dataframe otherwise

    #     Args:
    #         meteo (Dict): JSON input

    #     Returns:
    #         dict: response dataframe
    #     """

    #     meteo = self._jsonify(meteo)
    #     if format == 0 :
    #         if 'hourly' in meteo :
    #             if 'daily' in meteo :
    #                 return pd.DataFrame(meteo['hourly']), pd.DataFrame(meteo['daily'])
    #             else :
    #                 return pd.DataFrame(meteo['hourly'])
    #         else :
    #             if 'daily' in meteo :
    #                 return pd.DataFrame(meteo['daily'])
    #             else :
    #                 return pd.DataFrame(meteo)
    #     elif format == 1 :
    #         if 'hourly' in meteo :
    #             if 'daily' in meteo :
    #                 pd.DataFrame(meteo['hourly']).to_csv(filepath+"_hourly.csv")
    #                 pd.DataFrame(meteo['daily']).to_csv(filepath+"_daily.csv")
    #                 return pd.DataFrame(meteo['hourly']),pd.DataFrame(meteo['daily'])
    #             else :
    #                 pd.DataFrame(meteo['hourly']).to_csv(filepath+"_hourly.csv")
    #                 return pd.DataFrame(meteo['hourly'])
    #         else :
    #             if 'daily' in meteo :
    #                 pd.DataFrame(meteo['daily']).to_csv(filepath+"_daily.csv")
    #                 return pd.DataFrame(meteo['daily'])
    #             else :
    #                 pd.DataFrame(meteo).to_csv(filepath+".csv")
    #                 return pd.DataFrame(meteo)
    #     elif format == 2 :
    #         if 'hourly' in meteo :
    #             if 'daily' in meteo :
    #                 pd.DataFrame(meteo['hourly']).to_excel(filepath+"_hourly.xlsx")
    #                 pd.DataFrame(meteo['daily']).to_excel(filepath+"_daily.xlsx")
    #                 return pd.DataFrame(meteo['hourly']),pd.DataFrame(meteo['daily'])
    #             else :
    #                 pd.DataFrame(meteo['hourly']).to_excel(filepath+"_hourly.xlsx")
    #                 return pd.DataFrame(meteo['hourly'])
    #         else :
    #             if 'daily' in meteo :
    #                 pd.DataFrame(meteo['daily']).to_excel(filepath+"_daily.xlsx")
    #                 return pd.DataFrame(meteo['daily'])
    #             else :
    #                 pd.DataFrame(meteo).to_excel(filepath+".xlsx")
    #                 return pd.DataFrame(meteo)
    #     else :
    #         raise FileOptionError

    # # TODO: Find bug in this function to return a correct clean version of the original json response from the server
    # def _jsonify(self, res):
    #     """Returns a json with each variable having keys as dates, result json otherwise.

    #     Args:
    #         res (Dict): original JSON response from the server
    #     Returns:
    #         dict: clean JSON response
    #     """
    #     daily = {}
    #     hourly = {}
    #     cleaned_data = {}
    #     if "hourly" in res and "daily" in res:
    #         for i in res['hourly']:
    #             data = {}
    #             for j in range(len(res['hourly'][i])-1):
    #                 data[res["hourly"]["time"][j]] = res['hourly'][i][j]
    #             hourly[i] = data
    #         cleaned_data["hourly"] = hourly
    #         for i in res['daily']:
    #             data = {}
    #             for j in range(len(res['daily'][i])-1):
    #                 data[res["daily"]["time"][j]] = res['daily'][i][j]
    #             daily[i] = data
    #         cleaned_data["daily"] = daily
    #     elif "hourly" in res and "daily" not in res:
    #         for i in res['hourly']:
    #             data = {}
    #             for j in range(len(res['hourly'][i])-1):
    #                 data[res["hourly"]["time"][j]] = res['hourly'][i][j]
    #             hourly[i] = data
    #         cleaned_data["hourly"] = hourly
    #     elif "hourly" not in res and "daily" in res :
    #         for i in res['daily']:
    #             data = {}
    #             for j in range(len(res['daily'][i])-1):
    #                 data[res["daily"]["time"][j]] = res['daily'][i][j]
    #             daily[i] = data
    #         cleaned_data["daily"] = daily
    #     else :
    #         cleaned_data = res
    #     if "minutely_15" in res:
    #         for i in res['minutely_15']:
    #             data = {}
    #             for j in range(len(res['minutely_15'][i])-1):
    #                 data[res["minutely_15"]["time"][j]] = res['minutely_15'][i][j]
    #             daily[i] = data
    #         cleaned_data["minutely_15"] = daily
    #     return cleaned_data

    
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
        daily = {}
        hourly = {}
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


    def get_data(self, output = 0, file = 0, filepath = None):
        """
        Handles the retrieval and processing of the OPEN-METEO data.

        Args:
            output (int, optional): default is the server response JSON (option 0),
                                        1 for a JSON with variable keys as dates,
                                        2 for the server response parsed as a dataframe 
                                        3 for a dataframe where each column is for a variable with rows being linked each to a time/date
            file (int, optional):       0 as a default (not saving), 
                                        1 for the server's response JSON or dataframe saved as csv, 
                                        2 for excel file (xlsx)
            filepath (string, optional): filepath of the output file to be saved at

        Raises:
            BaseException: HTTP error
            ApiCallError: Api resonse error
            FileOptionError: File option being incorrect (number < 0 or > 3)
            FilepathNotFilled: Filepath not filled in the input options
            ConnectionError: requests connection error (internet connection or server having some trouble)

        Returns:
            dict: response JSON
        """

        try:
            r  = requests.get(self.url.value, params = self.payload)
            if r.status_code != 200 and r.status_code != 400:
                raise BaseException("Failed retrieving open-meteo data, server returned HTTP code: {} on following URL {}.".format(r.status_code, r.url))
            if "reason" in r :
                raise ApiCallError(r)
            if file == 0 :
                if output == 0 :
                    return json.loads(r.content.decode('utf-8'))
                elif output == 1 :
                    return self.Jsonify(json.loads(r.content.decode('utf-8')))
                elif output == 2 :
                    return pd.DataFrame(json.loads(r.content.decode('utf-8')))
                elif output == 3 :
                    return self.dataframit(json.loads(r.content.decode('utf-8')))
            elif file > 0 and file < 3 :
                if filepath == None :
                    raise FilepathNotFilled
                if output == 0 :
                    with open(filepath+'.json', 'wb+') as f:
                        f.write(r.content)
                    return json.loads(r.content.decode('utf-8'))
                elif output == 1 :
                    with open(filepath+'.json', 'wb+') as f:
                        f.write(r.content)
                    return self.Jsonify(json.loads(r.content.decode('utf-8')))
                elif output == 2 :
                    if file == 1 :
                        pd.DataFrame(json.loads(r.content.decode('utf-8'))).to_csv(filepath+".csv")
                        return pd.DataFrame(json.loads(r.content.decode('utf-8')))
                    else :
                        pd.DataFrame(json.loads(r.content.decode('utf-8'))).to_excel(filepath+".xlsx")
                        return pd.DataFrame(json.loads(r.content.decode('utf-8')))
                elif output == 3 :
                    if file == 1 :
                        return self.dataframit(json.loads(r.content.decode('utf-8')),file,filepath)
                    else :
                        return self.dataframit(json.loads(r.content.decode('utf-8')),file,filepath)
            else :
                raise FileOptionError
        except requests.ConnectionError as e :
            raise(e)