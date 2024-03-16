from openmeteo_py.exceptions import *

class FiftennMinutesDwd():

    """
    daily Parameter functions

    Aggregations are a simple 24 hour aggregation from hourly values. 

    """

    def __init__(self) :
        self.minutes_15_params = TypedList()

    def shortwave_radiation(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum  daily air temperature at 2 meters above ground
        """
        self.minutes_15_params.append("shortwave_radiation")
        return self
    
    def direct_normal_irradiance(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Minimum daily air temperature at 2 meters above ground
        """
        self.minutes_15_params.append("direct_normal_irradiance")
        return self

    def direct_radiation(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum dailt apparent temperature
        """
        self.minutes_15_params.append("direct_radiation")
        return self

    def diffuse_radiation(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Minimum dailt apparent temperature
        """
        self.minutes_15_params.append("diffuse_radiation")
        return self

    def lightning_potential(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Sum of daily precipitation
        """
        self.minutes_15_params.append("lightning_potential")
        return self

    def precipitation(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        The number of hours with rain
        """
        self.minutes_15_params.append("precipitation")
        return self

    def snowfall(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        The most severe weather condition on a given day
        """
        self.minutes_15_params.append("snowfall")
        return self

    def rain(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum wind speed  on a day
        """
        self.minutes_15_params.append("rain")
        return self

    def snowfall_height(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Maximum wind gusts on a day
        """
        self.minutes_15_params.append("snowfall_height")
        return self

    def freezinglevel_height(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        Dominant wind direction
        """
        self.minutes_15_params.append("freezinglevel_height")
        return self

    def cape(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        The sum of solar radiaion on a given day in Mega Joules
        """
        self.minutes_15_params.append("cape")
        return self
    
    def all(self):
        """
        Returns the daily configuration object 
        :returns: `hourly()`

        All parameters
        """
        self.minutes_15_params.append_all([
            "shortwave_radiation",                                                                             
            "direct_radiation",
            "direct_normal_irradiance",
            "diffuse_radiation",
            "lightning_potential",
            "precipitation",
            "snowfall",
            "rain",
            "snowfall_height",
            "freezinglevel_height",
            "cape"])
        return self