from openmeteopy import OpenMeteo
from openmeteopy.hourly import *
from openmeteopy.options import *
import requests

# Latitude, Longitude 
latitude =  -6.31
longitude = 33.89

def test_air_quality():
    # Set a class to specify hourly forecasts for the AirQuality system
    hourly = HourlyAirQuality()
    hourly = hourly.grass_pollen()
    # Set options to get specific forecasts
    options = AirQualityOptions(latitude, longitude, start_end=True, start_date='2024-03-19', end_date='2024-03-24') 
    # Set the OM client to fetch data
    mgr = OpenMeteo(options, hourly)
    # Fetch data
    data = mgr._fetch()
    
    assert data.status_code == 200

def test_dwd():
    hourly = HourlyDwd()
    hourly = hourly.cloudcover()
    options = DwdOptions(latitude, longitude)
    mgr = OpenMeteo(options, hourly)
    data = mgr._fetch()
    
    assert data.status_code == 200

def test_ecmwf():
    hourly = HourlyEcmwf()
    hourly = hourly.temperature_2m()
    options = EcmwfOptions(latitude, longitude, forecast_days=3) 
    mgr = OpenMeteo(options, hourly)
    data = mgr._fetch()
    
    assert data.status_code == 200

def test_forecast():
    hourly = HourlyForecast()
    hourly = hourly.winddirection_10m()
    options = ForecastOptions(latitude, longitude) 
    mgr = OpenMeteo(options, hourly)
    data = mgr._fetch()
    
    assert data.status_code == 200

def test_gem():
    hourly = HourlyGem()
    hourly = hourly.precipitation()
    options = GemOptions(latitude, longitude) 
    mgr = OpenMeteo(options, hourly)
    data = mgr._fetch()
    
    assert data.status_code == 200

def test_gfs():
    hourly = HourlyGfs()
    hourly = hourly.all()
    options = GfsOptions(latitude, longitude) 
    mgr = OpenMeteo(options, hourly)
    data = mgr._fetch()
    
    assert data.status_code == 200

def test_historical():
    hourly = HourlyHistorical()
    hourly = hourly.snowfall()
    options = HistoricalOptions(latitude, longitude, start_date='2019-02-12', end_date='2019-02-20') 
    mgr = OpenMeteo(options, hourly)
    data = mgr._fetch()
    
    assert data.status_code == 200

def test_jma():
    hourly = HourlyJma()
    hourly = hourly.temperature_350hpa()
    options = JmaOptions(latitude, longitude) 
    mgr = OpenMeteo(options, hourly)
    data = mgr._fetch()
    
    assert data.status_code == 200

def test_marine():
    marine_lat = 42
    marine_lon = -25
    hourly = HourlyMarine()
    hourly = hourly.wave_direction()
    # TODO: Check this option to accept only coordinates for ocean points
    options = MarineOptions(marine_lat, marine_lon) 
    mgr = OpenMeteo(options, hourly)
    data = mgr._fetch()
    
    assert data.status_code == 200

def test_meteo_france():
    hourly = HourlyMeteoFrance()
    hourly = hourly.snowfall()
    options = MeteoFranceOptions(latitude, longitude) 
    mgr = OpenMeteo(options, hourly)
    data = mgr._fetch()
    
    assert data.status_code == 200

def test_metno():
    metno_lat = 59.91
    metno_lon = 10.75
    # TODO: Same as for marine. No data available for the location of coordinates defined at the beginning of this module
    #       Specify that the locations for this option should be only scandinavian coordinates
    hourly = HourlyMetno()
    hourly = hourly.pressure_msl()
    options = MetnoOptions(metno_lat, metno_lon) 
    mgr = OpenMeteo(options, hourly)
    data = mgr._fetch()
    
    assert data.status_code == 200