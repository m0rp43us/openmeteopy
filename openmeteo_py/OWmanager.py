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
from openmeteo_py import ApiCallError,FilepathNotFilled,FileOptionError

def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except http.client.IncompleteRead as e:
            return e.partial
    return inner

http.client.HTTPResponse.read = patch_http_response_read(http.client.HTTPResponse.read)

class OWmanager():

    gem = "https://api.open-meteo.com/v1/gem?"
    metno = "https://api.open-meteo.com/v1/metno?"
    jma = "https://api.open-meteo.com/v1/jma?"
    dwd_icon = "https://api.open-meteo.com/v1/dwd-icon?"
    meteofrance = "https://api.open-meteo.com/v1/meteofrance?"
    gfs = "https://api.open-meteo.com/v1/gfs?"
    ecmwf = "https://api.open-meteo.com/v1/ecmwf?"
    historical = "https://archive-api.open-meteo.com/v1/archive?"
    marine = "https://marine-api.open-meteo.com/v1/marine?"
    air_quality = "https://air-quality-api.open-meteo.com/v1/air-quality?"
    geocoding = "https://geocoding-api.open-meteo.com/v1/search?"
    elevation = "https://api.open-meteo.com/v1/elevation?"
    flood = "https://flood-api.open-meteo.com/v1/flood?"
    forecast = "https://api.open-meteo.com/v1/forecast?"



    def __init__(self,options,api=None , hourly = None,daily = None, fifteen_minutes = None,api_key=None,):
        
        """
        Entry point class providing ad-hoc API clients for each OW web API.

        Args:
            options (Options): options for the /v1/forecast endpoint .
            hourly (Hourly): Hourly parameter object.
            daily (Daily) : Daily parameter object.
            api_key (string) : commercial API key.
        """
        #self.payload = {}
        self.options = options
        self.hourly = hourly
        self.daily = daily
        self.fifteen_minutes = fifteen_minutes
        if api != None :
            self.url = api
            if api == self.geocoding :
                self.payload = {
                    "name": options.name,
                    "count": options.count,
                    "format": options.format,
                    "language" : options.language
                    }
            elif api == self.elevation:
                self.payload = {
                    "latitude": options.latitude,
                    "longitude": options.longitude
                    }
            elif api == self.marine:
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
            elif api == self.gem:
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
            elif api == self.metno:
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
            elif api == self.flood:
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
            elif api == self.meteofrance or api == self.jma or api == self.dwd_icon :
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
            elif api == self.ecmwf:
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
            elif api == self.forecast:
                self.payload = {
                        "latitude": options.latitude,
                        "longitude": options.longitude,
                        "timezone": options.timezone,
                        "windspeed_unit":options.windspeed_unit,
                        "precipitation_unit":options.precipitation_unit,
                        "timeformat":options.timeformat,
                        "past_days":options.past_days
                        }
            elif api == self.gfs:
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
            elif api == self.historical:
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
            elif api == self.air_quality:
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

    def Jsonify(self,meteo):
        """Returns a json with each variable having keys as dates,result json otherwise

        Args:
            meteo (Dict): JSON input

        Returns:
            dict: response JSON
        """

        daily = {}
        hourly = {}
        cleaned_data = {}
        if "hourly" in meteo and "daily" in meteo:
            for i in meteo['hourly']:
                data = {}
                for j in range(len(meteo['hourly'][i])-1):
                    data[meteo["hourly"]["time"][j]] = meteo['hourly'][i][j]
                hourly[i] = data
            cleaned_data["hourly"] = hourly
            for i in meteo['daily']:
                data = {}
                for j in range(len(meteo['daily'][i])-1):
                    data[meteo["daily"]["time"][j]] = meteo['daily'][i][j]
                daily[i] = data
            cleaned_data["daily"] = daily
        elif "hourly" in meteo and "daily" not in meteo:
            for i in meteo['hourly']:
                data = {}
                for j in range(len(meteo['hourly'][i])-1):
                    data[meteo["hourly"]["time"][j]] = meteo['hourly'][i][j]
                hourly[i] = data
            cleaned_data["hourly"] = hourly
        elif "hourly" not in meteo and "daily" in meteo :
            for i in meteo['daily']:
                data = {}
                for j in range(len(meteo['daily'][i])-1):
                    data[meteo["daily"]["time"][j]] = meteo['daily'][i][j]
                daily[i] = data
            cleaned_data["daily"] = daily
        else :
            cleaned_data = meteo
        if "minutely_15" in meteo  :
            for i in meteo['minutely_15']:
                data = {}
                for j in range(len(meteo['minutely_15'][i])-1):
                    data[meteo["minutely_15"]["time"][j]] = meteo['minutely_15'][i][j]
                daily[i] = data
            cleaned_data["minutely_15"] = daily
        return cleaned_data


    def get_data(self,output = 0,file = 0,filepath = None):
        """
        Handles the retrieval and processing of the OPEN-METEO data.

        Args:
            output (int, optional): default is the server response JSON (option 0),1 for a JSON with variable keys as dates,2 for the server response parsed as a dataframe and 3 for a dataframe where each column is for a variable with rows being linked each to a time/date
            file (int, optional): 0 as a default (not saving),1 for the server's response JSON or dataframe saved as csv,2 for excel file (xlsx)
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
            r  = requests.get(self.url, params = self.payload)
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
    
    def dataframit(self,meteo,format = 0,filepath = None):
        """Returns a dataframe with each variable having keys as dates,result dataframe otherwise

        Args:
            meteo (Dict): JSON input

        Returns:
            dict: response dataframe
        """

        meteo = self.Jsonify(meteo)
        if format == 0 :
            if 'hourly' in meteo :
                if 'daily' in meteo :
                    return pd.DataFrame(meteo['hourly']),pd.DataFrame(meteo['daily'])
                else :
                    return pd.DataFrame(meteo['hourly'])
            else :
                if 'daily' in meteo :
                    return pd.DataFrame(meteo['daily'])
                else :
                    return pd.DataFrame(meteo)
        elif format == 1 :
            if 'hourly' in meteo :
                if 'daily' in meteo :
                    pd.DataFrame(meteo['hourly']).to_csv(filepath+"_hourly.csv")
                    pd.DataFrame(meteo['daily']).to_csv(filepath+"_daily.csv")
                    return pd.DataFrame(meteo['hourly']),pd.DataFrame(meteo['daily'])
                else :
                    pd.DataFrame(meteo['hourly']).to_csv(filepath+"_hourly.csv")
                    return pd.DataFrame(meteo['hourly'])
            else :
                if 'daily' in meteo :
                    pd.DataFrame(meteo['daily']).to_csv(filepath+"_daily.csv")
                    return pd.DataFrame(meteo['daily'])
                else :
                    pd.DataFrame(meteo).to_csv(filepath+".csv")
                    return pd.DataFrame(meteo)
        elif format == 2 :
            if 'hourly' in meteo :
                if 'daily' in meteo :
                    pd.DataFrame(meteo['hourly']).to_excel(filepath+"_hourly.xlsx")
                    pd.DataFrame(meteo['daily']).to_excel(filepath+"_daily.xlsx")
                    return pd.DataFrame(meteo['hourly']),pd.DataFrame(meteo['daily'])
                else :
                    pd.DataFrame(meteo['hourly']).to_excel(filepath+"_hourly.xlsx")
                    return pd.DataFrame(meteo['hourly'])
            else :
                if 'daily' in meteo :
                    pd.DataFrame(meteo['daily']).to_excel(filepath+"_daily.xlsx")
                    return pd.DataFrame(meteo['daily'])
                else :
                    pd.DataFrame(meteo).to_excel(filepath+".xlsx")
                    return pd.DataFrame(meteo)
        else :
            raise FileOptionError