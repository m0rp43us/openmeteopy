from openmeteo_py import OWmanager
from openmeteo_py.Hourly.HourlyAirQuality import HourlyAirQuality
from openmeteo_py.Options.AirQualityOptions import AirQualityOptions
from openmeteo_py.Utils.constants import *

# Latitude, Longitude 
longitude = 33.89
latitude =  -6.31

hourly = HourlyAirQuality()
options = AirQualityOptions(latitude,longitude,auto)

#notice that we had to give the value "None" for the hourly parameter,otherwise you'll be filling the hourly parameter instead of the daily one.
mgr = OWmanager(options,OWmanager.air_quality,hourly.all())


# Download data,here we want it as a key value json where the keys are dates and values the corresponding values of that date (technically timestamp)
meteo = mgr.get_data(1)

print(meteo)