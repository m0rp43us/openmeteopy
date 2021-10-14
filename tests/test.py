print(__name__)
import pandas as pd
import time

from openmeteo_py import Hourly,Daily,OWmanager,Options

# Latitude, Longitude for Rabat,Morocco
latitude = 33.9842
longitude = -6.8675

hourly = Hourly()
daily = Daily()
options = Options(latitude,longitude)

mgr = OWmanager(options,
    hourly.cloudcover_mid(),
    daily.temperature_2m_max())


# Download data
meteo = mgr.get_data(1,1,"/home/morpheus/openmeteopy/output")



'''
options :
1 - response JSON
2 - JSON with keys for each variable as the date/time,value is the value at that precise time/date
3 - response as a dataframe
4 - Dataframe as date/value for each variable (each variable has its own dataframe)
/file = true :
save the outpute as a file,depending on the output could be a dataframe or a json file,could also be an xls file or netcdf ...
'''
print(str(meteo['hourly']['cloudcover_mid'])+'\n')
print(str(meteo['daily']['temperature_2m_max'])+'\n')