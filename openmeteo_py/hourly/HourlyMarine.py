from openmeteo_py.exceptions import *


class HourlyMarine()  :

    """
    hourly Parameter functions

    hourly Parameter Definition
    Most weather variables are given as an instantaneous value for the indicated hour. 
    Some variables like precipitation are calculated from the preceding hour as and average or sum.

    """


    def __init__(self) :
        self.hourly_params = TypedList()

    def wave_height(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

         	Wave height of significant mean
        """

        self.hourly_params.append("wave_height")
        return self

    def wave_direction(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`
        
        Relative humidity at 2 meters above ground
        
        """
        self.hourly_params.append("wave_direction")
        return self

    def wave_period(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Dew point temperature at 2 meters above ground
        
        """

        self.hourly_params.append("wave_period")
        return self

    def wind_wave_height(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Wind wave height of significant mean

        
        """

        self.hourly_params.append("wind_wave_height")
        return self

    def wind_wave_direction(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Mean direction of wind waves
        
        """

        self.hourly_params.append("wind_wave_direction")
        return self

    def wind_wave_period(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Period between mean wind waves
        
        """

        self.hourly_params.append("wind_wave_period")
        return self

    def wind_wave_peak_period(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between wind waves.
        
        """

        self.hourly_params.append("wind_wave_peak_period")
        return self

    def swell_wave_height(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Swell  wave height of significant mean

        
        """

        self.hourly_params.append("swell_wave_height")
        return self

    def swell_wave_direction(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

         	Mean direction of swell waves
        
        """

        self.hourly_params.append("swell_wave_direction")
        return self

    def swell_wave_period(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Period between mean swell waves

        
        """

        self.hourly_params.append("swell_wave_period")
        return self

    def swell_wave_peak_period(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("swell_wave_peak_period")
        return self

    
    def all(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        All hourly parameters
        """
        self.hourly_params.append_all(
            ["wave_height",
             "wave_direction",
             "wave_period",
             "wind_wave_height",
             "wind_wave_direction",
             "wind_wave_period",
             "wind_wave_peak_period",
             "swell_wave_height",
             "swell_wave_direction",
             "swell_wave_period",
             "swell_wave_peak_period"])
        return self