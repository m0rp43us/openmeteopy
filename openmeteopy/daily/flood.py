from openmeteopy.exceptions import *

class DailyFlood():

    """
    daily Parameter functions

    Aggregations are a simple 24 hour aggregation from hourly values. 

    """

    def __init__(self) :
        self.daily_params = TypedList()

    def river_discharge(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum  daily air temperature at 2 meters above ground
        """
        self.daily_params.append("river_discharge")
        return self
    
    def river_discharge_mean(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

         	daily maximum in UV Index starting from 0
        """
        self.daily_params.append("river_discharge_mean")
        return self
    
    def river_discharge_median(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        uv_index_clear_sky_max assumes cloud free conditions. Please follow the official WMO guidelines for ultraviolet index.
        """
        self.daily_params.append("river_discharge_median")
        return self

    def river_discharge_max(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Minimum daily air temperature at 2 meters above ground
        """
        self.daily_params.append("river_discharge_max")
        return self

    def river_discharge_min(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum dailt apparent temperature
        """
        self.daily_params.append("river_discharge_min")
        return self

    def river_discharge_p25(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Minimum dailt apparent temperature
        """
        self.daily_params.append("river_discharge_p25")
        return self

    def river_discharge_p75(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Sum of daily precipitation
        """
        self.daily_params.append("river_discharge_p75")
        return self
    
    def all(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        All parameters
        """
        self.daily_params.append_all([
            "river_discharge",
            "river_discharge_mean",
            "river_discharge_median",
            "river_discharge_max",
            "river_discharge_min",
            "river_discharge_p25",
            "river_discharge_p75"])
        return self