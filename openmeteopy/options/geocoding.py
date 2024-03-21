from openmeteopy.utils.constants import *
from openmeteopy.utils.timezones import *
from openmeteopy.utils.languages import en
from .option import Option

class GeocodingOptions(Option):
    API_PATH = "https://geocoding-api.open-meteo.com/v1/search?"
    """

    The API options accepts a WGS4 coordinate and other  weather variables .
    Time always starts at 0:00 today and contains 168 hours.

    """
    def __init__(self, name, count=10,format=json,language=en):
        """
        Args:
            name (String): String to search for. An empty string or only 1 character will return an empty result. 2 characters will only match exact matching locations. 3 and more characters will perform fuzzy matching. The search string can be a location name or a postal code.
            count (Integer): The number of search results to return. Up to 100 results can be retrieved.
        """
        
        self.name = name
        self.count = count
        self.format = format
        self.language = language
    
    def get_api_path(self):
        return self.API_PATH
    
    def get_payload(self):
        payload = {
            "name": self.name,
            "count": self.count,
            "format": self.format,
            "language" : self.language
            }
        return payload