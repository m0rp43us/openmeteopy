print(__name__)
import pandas as pd
import time

from openmeteo_py.Hourly import Hourly 
from openmeteo_py.Daily import Daily 
from openmeteo_py.Options import Options
from openmeteo_py.OWmanager import OWmanager
# Latitude, Longitude for Rabat,Morocco
latitude = 33.9842
longitude = -6.8675

hourly = Hourly()
daily = Daily()
options = Options(latitude,longitude)

mgr = OWmanager(options,
    hourly.all(),
    daily.all())


# Download data
meteo = mgr.get_data()

#response as a simple json
#print(meteo)

#response as a dataframe
#print(pd.DataFrame(meteo))

#for element in meteo:
#    if element == 'hourly':
#        print(len(meteo['hourly']))
#        for i in meteo['hourly']:
#            print(meteo['hourly'][i])

'''
optinos :
1 - response JSON
2 - JSON with keys for each variable as the date/time,value is the value at that precise time/date
3 - response as a dataframe
4 - Dataframe as date/value for each variable (each variable has its own dataframe)
/file = true :
save the outpute as a file,depending on the output could be a dataframe or a json file,could also be an xls file or netcdf ...
'''
#preparing the dataframe
#daily = {}
#hourly = {}
#cleaned_data = {}
#if "hourly" in meteo and "daily" in meteo:
#    for i in meteo['hourly']:
#        print(meteo['hourly'][i])
#        data = {}
#        for j in range(len(meteo['hourly'][i])-1):
#            data[meteo["hourly"]["time"][j]] = meteo['hourly'][i][j]
#        hourly[i] = data
#    cleaned_data["hourly"] = hourly
#    for i in meteo['daily']:
#        data = {}
#        for j in range(len(meteo['daily'][i])-1):
#            data[meteo["daily"]["time"][j]] = meteo['daily'][i][j]
#        daily[i] = data
#    cleaned_data["daily"] = daily
#elif "hourly" in meteo and "daily" not in meteo:
#    for i in meteo['hourly']:
#        print(meteo['hourly'][i])
#        data = {}
#        for j in range(len(meteo['hourly'][i])-1):
#            data[meteo["hourly"]["time"][j]] = meteo['hourly'][i][j]
#        hourly[i] = data
#    cleaned_data["hourly"] = hourly
#elif "hourly" not in meteo and "daily" in meteo :
#    for i in meteo['daily']:
#        data = {}
#        for j in range(len(meteo['daily'][i])-1):
#            data[meteo["daily"]["time"][j]] = meteo['daily'][i][j]
#        daily[i] = data
#    cleaned_data["daily"] = daily
#else :
#    print("neither hourly nor daily")

#print(cleaned_data)
#print(pd.DataFrame(cleaned_data["hourly"]))

print(meteo)