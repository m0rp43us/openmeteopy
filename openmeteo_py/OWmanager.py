"""
A module for downloading meteorological data from the open-meteo API (https://open-meteo.com/en/).
Name: Wail Chalabi
e-mail: wail.agroconcept@gmail.com
Version: 0.0.1
"""

import http.client
import requests
import json
import pandas as pd
from openmeteo_py.Options import Options
from openmeteo_py.Daily import Daily
from openmeteo_py.Hourly import Hourly
from openmeteo_py.utils import ApiCallError
from openmeteo_py.utils import FilepathNotFilled,FileOptionError
def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except http.client.IncompleteRead as e:
            return e.partial
    return inner

http.client.HTTPResponse.read = patch_http_response_read(http.client.HTTPResponse.read)

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

    def Jsonify(self,meteo):
        #preparing the dataframe
        daily = {}
        hourly = {}
        cleaned_data = {}
        if "hourly" in meteo and "daily" in meteo:
            for i in meteo['hourly']:
                print(meteo['hourly'][i])
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
                print(meteo['hourly'][i])
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
        return cleaned_data


    def get_data(self,output = 0,file = 0,filepath = None):
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
            elif file > 0 and file < 4 :
                if filepath == None :
                    raise FilepathNotFilled
                if output == 0 :
                    with open(file+'.json', 'wb+') as f:
                        f.write(r.content)
                    return json.loads(r.content.decode('utf-8'))
                elif output == 1 :
                    with open(file+'.json', 'wb+') as f:
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

