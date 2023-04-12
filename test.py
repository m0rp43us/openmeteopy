
#from openmeteo_py.Daily.Marine import Marine as Daily
from openmeteo_py import OWmanager
from openmeteo_py.Hourly.HourlyHistorical import HourlyHistorical
from openmeteo_py.Daily.DailyHistorical import DailyHistorical
from openmeteo_py.Options.HistoricalOptions import HistoricalOptions
from openmeteo_py.Utils.constants import *

# Latitude, Longitude 
longitude = 33.89
latitude =  -6.31

hourly = HourlyHistorical()
daily = DailyHistorical()
options = HistoricalOptions(latitude,longitude,nan,False,celsius,kmh,mm,iso8601,utc,"2022-12-31","2023-02-26")

#notice that we had to give the value "None" for the hourly parameter,otherwise you'll be filling the hourly parameter instead of the daily one.
mgr = OWmanager(options,OWmanager.historical,hourly.all(),daily.all())


# Download data,here we want it as a key value json where the keys are dates and values the corresponding values of that date (technically timestamp)
meteo = mgr.get_data(1)

print(meteo)