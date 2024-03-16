from openmeteo_py import OpenMeteo
from openmeteo_py.hourly.HourlyEcmwf import HourlyEcmwf
from openmeteo_py.options.EcmwfOptions import EcmwfOptions
from openmeteo_py.utils.constants import *
import requests

# Latitude, Longitude 
latitude =  -6.31
longitude = 33.89

# Set a class to specify hourly forecasts for the ECMWF system
hourly = HourlyEcmwf()
hourly = hourly.winddirection_10m()
hourly = hourly.temperature_2m()
# Set options to get specific forecasts
options = EcmwfOptions(latitude, 
                        longitude,
                        forecast_days=3) 
    
# Set the OM client to fetch data
mgr = OpenMeteo(options, "ecmwf", hourly)
print(mgr.url, mgr.payload)
# Fetch data
res_json = mgr.get_json()
print(res_json)

res_pd = mgr.get_pandas()
print(res_pd)