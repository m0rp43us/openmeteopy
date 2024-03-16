from openmeteo_py.exceptions import *



class HourlyAirQuality()  :

    """
    hourly Parameter functions

    hourly Parameter Definition
    Most weather variables are given as an instantaneous value for the indicated hour. 
    Some variables like precipitation are calculated from the preceding hour as and average or sum.

    """


    def __init__(self) :
        self.hourly_params = TypedList()

    def pm10(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

         	Wave height of significant mean
        """

        self.hourly_params.append("pm10")
        return self

    def pm2_5(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`
        
        Relative humidity at 2 meters above ground
        
        """
        self.hourly_params.append("pm2_5")
        return self

    def carbon_monoxide(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Dew point temperature at 2 meters above ground
        
        """

        self.hourly_params.append("carbon_monoxide")
        return self

    def nitrogen_dioxide(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Wind wave height of significant mean

        
        """

        self.hourly_params.append("nitrogen_dioxide")
        return self

    def sulphur_dioxide(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Mean direction of wind waves
        
        """

        self.hourly_params.append("sulphur_dioxide")
        return self

    def ozone(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Period between mean wind waves
        
        """

        self.hourly_params.append("ozone")
        return self

    def ammonia(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between wind waves.
        
        """

        self.hourly_params.append("ammonia")
        return self

    def aerosol_optical_depth(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Swell  wave height of significant mean

        
        """

        self.hourly_params.append("aerosol_optical_depth")
        return self

    def dust(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

         	Mean direction of swell waves
        
        """

        self.hourly_params.append("dust")
        return self

    def uv_index(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Period between mean swell waves

        
        """

        self.hourly_params.append("uv_index")
        return self

    def uv_index_clear_sky(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("uv_index_clear_sky")
        return self

#start 

    def alder_pollen(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("alder_pollen")
        return self
    
    def birch_pollen(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("birch_pollen")
        return self
    
    def grass_pollen(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("grass_pollen")
        return self
    
    def mugwort_pollen(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("mugwort_pollen")
        return self
    
    def olive_pollen(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("olive_pollen")
        return self
    
    def ragweed_pollen(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("ragweed_pollen")
        return self
    
    def european_aqi(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("european_aqi")
        return self
    
    def european_aqi_pm2_5(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("european_aqi_pm2_5")
        return self
    
    def european_aqi_pm10(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("european_aqi_pm10")
        return self
    #end
    
    def european_aqi_no2(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("european_aqi_no2")
        return self
    
    def european_aqi_o3(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("european_aqi_o3")
        return self
    
    def european_aqi_so2(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("european_aqi_so2")
        return self
    
    def us_aqi(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("us_aqi")
        return self
    
    def us_aqi_pm2_5(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("us_aqi_pm2_5")
        return self
    
    def us_aqi_pm2_5(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("us_aqi_pm2_5")
        return self
    
    def us_aqi_pm10(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("us_aqi_pm10")
        return self
    
    def us_aqi_no2(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("us_aqi_no2")
        return self
    
    def us_aqi_o3(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("us_aqi_o3")
        return self
    
    def us_aqi_so2(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("us_aqi_so2")
        return self
    
    def us_aqi_co(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Peak period between swell waves
        
        """

        self.hourly_params.append("us_aqi_co")
        return self
    
    def europe_air_quality_index(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        All hourly parameters
        """
        self.hourly_params.append_all(
            [
             "european_aqi",
             "european_aqi_pm2_5",
             "european_aqi_pm10",
             "european_aqi_no2",
             "european_aqi_o3",
             "european_aqi_so2"])
        return self
    
    def us_air_quality_index(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        All hourly parameters
        """
        self.hourly_params.append_all(
            ["us_aqi",
             "us_aqi_pm2_5",
             "us_aqi_pm10",
             "us_aqi_no2",
             "us_aqi_co",
             "us_aqi_o3",
             "us_aqi_so2"])
        return self
    
    def all(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        All hourly parameters
        """
        self.hourly_params.append_all(
            ["pm10",
             "pm2_5",
             "carbon_monoxide",
             "nitrogen_dioxide",
             "sulphur_dioxide",
             "ozone,aerosol_optical_depth",
             "dust","uv_index",
             "uv_index_clear_sky",
             "ammonia",
             "alder_pollen",
             "birch_pollen",
             "grass_pollen",
             "mugwort_pollen",
             "olive_pollen",
             "ragweed_pollen",
             "european_aqi",
             "european_aqi_pm2_5",
             "european_aqi_pm10",
             "european_aqi_no2",
             "european_aqi_o3",
             "european_aqi_so2",
             "us_aqi",
             "us_aqi_pm2_5",
             "us_aqi_pm10",
             "us_aqi_no2",
             "us_aqi_co",
             "us_aqi_o3",
             "us_aqi_so2"])
        return self