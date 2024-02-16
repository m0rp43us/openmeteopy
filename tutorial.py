from openmeteo_py import OWmanager
from openmeteo_py.Hourly.HourlyEcmwf import HourlyEcmwf
from openmeteo_py.Options.EcmwfOptions import EcmwfOptions
from openmeteo_py.Utils.constants import *

# Latitude, Longitude 
latitude =  -6.31
longitude = 33.89
start_date = '2024-01-30'
end_date = '2024-02-01'

# Set a class to specify hourly forecasts for the ECMWF system
hourly = HourlyEcmwf()
# Set options to get specific forecasts
options = EcmwfOptions(latitude, 
                       longitude,
                       forecast_days=5) 
                    #    start_end=True, # Set this flag true to get specific time window data 
                    #    start_date=start_date, 
                    #    end_date=end_date) 

# Set the OM client to fetch data
mgr = OWmanager(options, OWmanager.ecmwf, hourly.all())
# Fetch data
meteo = mgr.get_data()

print(meteo)