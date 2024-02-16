from openmeteo_py import OWmanager
from openmeteo_py.Hourly.HourlyEcmwf import HourlyEcmwf
from openmeteo_py.Options.EcmwfOptions import EcmwfOptions
from openmeteo_py.Utils.constants import *
import requests

# Latitude, Longitude 
latitude =  -6.31
longitude = 33.89

def test_row_json_forecasts():
    start_date = '2024-01-30'
    end_date = '2024-02-01'
    # Set a class to specify hourly forecasts for the ECMWF system
    hourly = HourlyEcmwf()
    # Set options to get specific forecasts
    options = EcmwfOptions(latitude, 
                        longitude, 
                        start_end=True, # Set this flag true to get specific time window data 
                        start_date=start_date, 
                        end_date=end_date) 
    
    # Call OM api and check that fetching data is ok 
    API_URL = 'https://api.open-meteo.com/v1/ecmwf?latitude=-6.31&longitude=33.89&elevation=nan&timeformat=iso8601&past_days=0&temperature_unit=celsius&current_weather=False&windspeed_unit=kmh&precipitation_unit=mm&start_date=2024-01-30&end_date=2024-02-01&cell_selection=land&hourly=precipitation'
    res = requests.get(API_URL)
    # Set the OM client to fetch data
    mgr = OWmanager(options, OWmanager.ecmwf, hourly.precipitation())
    # Fetch data
    meteo = mgr.get_data()
            
    assert meteo['hourly'] == res.json()['hourly']

def test_row_json_historical():
    start_date = '2024-01-30'
    end_date = '2024-02-01'
    # Set a class to specify hourly forecasts for the ECMWF system
    hourly = HourlyEcmwf()
    # Set options to get specific forecasts
    options = EcmwfOptions(latitude, 
                        longitude, 
                        start_end=True, # Set this flag true to get specific time window data 
                        start_date=start_date, 
                        end_date=end_date) 
    
    # Call OM api and check that fetching data is ok 
    API_URL = 'https://api.open-meteo.com/v1/ecmwf?latitude=-6.31&longitude=33.89&elevation=nan&timeformat=iso8601&past_days=0&temperature_unit=celsius&current_weather=False&windspeed_unit=kmh&precipitation_unit=mm&start_date=2024-01-30&end_date=2024-02-01&cell_selection=land&hourly=precipitation'
    res = requests.get(API_URL)
    # Set the OM client to fetch data
    mgr = OWmanager(options, OWmanager.ecmwf, hourly.precipitation())
    # Fetch data
    meteo = mgr.get_data()
            
    assert meteo['hourly'] == res.json()['hourly']