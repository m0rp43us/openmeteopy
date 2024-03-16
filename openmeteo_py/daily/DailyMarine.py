from openmeteo_py.exceptions import *

class DailyMarine():

    """
    daily Parameter functions

    Aggregations are a simple 24 hour aggregation from hourly values. 

    """

    def __init__(self) :
        self.daily_params = TypedList()

    def wave_height_max(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum wave height on a given day for the mean waves
        """
        self.daily_params.append("wave_height_max")
        return self
    
    def wind_wave_height_max(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum wave height on a given day for wind waves
        """
        self.daily_params.append("wind_wave_height_max")
        return self
    
    def swell_wave_height_max(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum wave height on a given day for swell waves.
        """
        self.daily_params.append("swell_wave_height_max")
        return self

    def wave_direction_dominant(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Dominant wave direction of mean if swell and wind waves.
        """
        self.daily_params.append("wave_direction_dominant")
        return self

    def wind_wave_direction_dominant(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Dominant wave direction of wind waves
        """
        self.daily_params.append("wind_wave_direction_dominant")
        return self

    def swell_wave_direction_dominant(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Dominant wave direction of swell waves
        """
        self.daily_params.append("swell_wave_direction_dominant")
        return self

    def wave_period_max(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum wave period of mean, wind and swell
        """
        self.daily_params.append("wave_period_max")
        return self

    def wind_wave_period_max(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum wave period of wind waves
        """
        self.daily_params.append("wind_wave_period_max")
        return self

    def swell_wave_period_max(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum wave period of swell waves
        """
        self.daily_params.append("swell_wave_period_max")
        return self

    def wind_wave_peak_period_max(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum peak period between wind waves
        """
        self.daily_params.append("wind_wave_peak_period_max")
        return self

    def swell_wave_peak_period_max(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum peak period between swell waves
        """
        self.daily_params.append("swell_wave_peak_period_max")
        return self
    
    def all(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        All parameters
        """
        self.daily_params.append_all([
            "swell_wave_peak_period_max",                                                                             
            "wind_wave_peak_period_max",
            "swell_wave_period_max",
            "wind_wave_period_max",
            "wave_period_max",
            "swell_wave_direction_dominant",
            "wind_wave_direction_dominant",
            "wave_direction_dominant",
            "swell_wave_height_max",
            "wind_wave_height_max",
            "wave_height_max"])
        return self