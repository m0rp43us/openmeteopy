from openmeteo_py.utils.constants import *
from openmeteo_py.utils.timezones import *



class FloodOptions():
    """

    The API options accepts a WGS4 coordinate and other  weather variables .
    Time always starts at 0:00 today and contains 168 hours.

    """
    def __init__(self, latitude, longitude,timeformat = iso8601,past_days = 0,forecast_days = 92,start_end = False,start_date = None,end_date = None,ensemble = False,cell_selection = nearest):
        """
        Args:
            latitude (float): Latitude (Geographical WGS84 coordiante of the location).
            longitude (float): Longitude (Geographical WGS84 coordiante of the location).
            timeformat (string, optional): If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. 
                                            Please note that all time is then in UTC! For daily values with unix timestamp, please apply utc_offset_seconds again to get the correct date.
            past_days (int, optional):  If past_days is set, yesterdays or the day before yesterdays data are also returned..
        Raises:
            ValueError: Raises when latitude is not between -90 and 90 degrees.
            ValueError: Raises when longitude is not between -180 and 180 degrees.
        """
        if latitude < -90 or latitude > 90:
            raise ValueError("Latitude should be between -90 and 90 degrees.")
        if longitude < -180 or longitude > 180:
            raise ValueError("Longitude should be between -180 and 180 degrees.")
        
        self.latitude = latitude
        self.longitude = longitude
        self.forecast_days = forecast_days
        self.ensemble = ensemble
        self.timeformat = timeformat
        self.cell_selection = cell_selection
        self.past_days = past_days
        if start_end != False :
                    self.start_date = start_date
                    self.end_date = end_date
                    self.start_end = start_end
        self.start_end = start_end
