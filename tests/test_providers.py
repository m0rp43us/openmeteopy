# from openmeteopy import OpenMeteo
# from openmeteopy.hourly import HourlyEcmwf
# from openmeteopy.options import EcmwfOptions
# from openmeteopy.utils.constants import *
# import requests

# # Latitude, Longitude 
# latitude =  -6.31
# longitude = 33.89

# def test_row_json_forecasts():
#     # Set a class to specify hourly forecasts for the ECMWF system
#     hourly = HourlyEcmwf()
#     hourly = hourly.temperature_2m()
#     # Set options to get specific forecasts
#     options = EcmwfOptions(latitude, 
#                            longitude,
#                            forecast_days=3) 
        
#     # Set the OM client to fetch data
#     mgr = OpenMeteo(options, hourly)
#     # Fetch data
#     data = mgr._fetch()
    
#     print(data)