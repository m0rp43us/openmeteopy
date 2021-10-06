from constants import *
from timezones import *



class Forcast():

    def __init__(self, latitude, longitude,timeformat = iso8601, timezone = UTC, windspeed_unit =kmh ,  precipitation_unit = mm,current_weather = False,past_days = 0):

        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude should be between -90 and 90 degrees.")
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude should be between -180 and 180 degrees.")
        
        self.latitude = latitude
        self.longitude = longitude
        self.windspeed_unit = windspeed_unit
        self.precipitation_unit = precipitation_unit
        self.timeformat = timeformat
        self.timezone = timezone
        self.current_weather = current_weather
        self.past_days = past_days
        