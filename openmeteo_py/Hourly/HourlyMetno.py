from openmeteo_py.Exceptions import *



class HourlyMetno()  :

    """
    Hourly Parameter functions

    Hourly Parameter Definition
    Most weather variables are given as an instantaneous value for the indicated hour. 
    Some variables like precipitation are calculated from the preceding hour as and average or sum.

    """


    def __init__(self) :
        self.hourly_params = TypedList()

    def temperature_2m(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Air temperature at 2 meters above ground
        """

        self.hourly_params.append("temperature_2m")
        return self

    def relativehumidity_2m(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`
        
        Relative humidity at 2 meters above ground
        
        """
        self.hourly_params.append("relativehumidity_2m")
        return self

    def dewpoint_2m(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Dew point temperature at 2 meters above ground
        
        """

        self.hourly_params.append("dewpoint_2m")
        return self

    def apparent_temperature(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Apparent temperature is the perceived feels-like tempertature combinding wind chill factor, realtive humidity and solar radition

        
        """

        self.hourly_params.append("apparent_temperature")
        return self

    def pressure_msl(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Atmospheric air pressure reduced to sea level
        
        """

        self.hourly_params.append("pressure_msl")
        return self

    def cloudcover(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Total cloud cover as an area fraction
        
        """

        self.hourly_params.append("cloudcover")
        return self

    def windspeed_10m(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Wind speed at 10 meters above ground. Wind speed on 10 meters is the standard level.

        
        """

        self.hourly_params.append("windspeed_10m")
        return self


    def winddirection_10m(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Wind direction at 10 meters above ground
        """

        self.hourly_params.append("winddirection_10m")
        return self

    def windgusts_10m(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Gusts at 10 meters above ground as a maximum of the preceding hour
        """

        self.hourly_params.append("windgusts_10m")
        return self

    def shortwave_radiation(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Shortwave solar radiation as average of the preceding hour
        """

        self.hourly_params.append("shortwave_radiation")
        return self

    def direct_radiation(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Direct solar radiation as average of the preceding hour
        """

        self.hourly_params.append("irect_radiation")
        return self

    def diffuse_radiation(self):
        """
        Returns the Hourly configuration object
        :returns: `Hourly()`

        Diffure solar radiation as average of the preceding hour
        """

        self.hourly_params.append("diffuse_radiation")
        return self

    def vapor_pressure_deficit(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Vapor Pressure Deificit (VPD) in kilo pascal (kPa). For high VPD (>1.6), water transpiration of plants increases. For low VPD (<0.4), transpiration decreases
        """

        self.hourly_params.append("vapor_pressure_deficit")
        return self

    def et0_fao_evapotranspiration(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Sum of evapotranspration of the preceding hour from lands urface and plants
        """

        self.hourly_params.append("et0_fao_evapotranspiration")
        return self

    def precipitation(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Total precipitation (rain, showers, snow) sum of the preceding hour
        """

        self.hourly_params.append("precipitation")
        return self

    def weathercode(self):
        """
        Returns the Hourly configuration object
        :returns: `Hourly()`

        Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details.
        """

        self.hourly_params.append("weathercode")
        return self



    def snowfall(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7.
        """
        self.hourly_params.append("snowfall")
        return self
    
    def soil_moisture_27_81cm(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Average soil water content as volumetric mixing ratio at 27-81 cm depths.
        """
        self.hourly_params.append("soil_moisture_27_81cm")
        return self
    
    def direct_normal_irradiance(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane.
        """
        self.hourly_params.append("direct_normal_irradiance")
        return self
    
    def direct_radiation(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane.
        """
        self.hourly_params.append("direct_radiation")
        return self
    
    def all(self):
        """
        Returns the Hourly configuration object 
        :returns: `Hourly()`

        All hourly parameters
        """
        self.hourly_params.append_all(
            ["temperature_2m",
            "relativehumidity_2m",
            "dewpoint_2m",
            "apparent_temperature",
            "pressure_msl",
            "surface_pressure",
            "cloudcover",
            "windspeed_10m",
            "winddirection_10m",
            "windgusts_10m",
            "shortwave_radiation",
            "direct_radiation",
            "diffuse_radiation",
            "vapor_pressure_deficit",
            "et0_fao_evapotranspiration",
            "precipitation",
            "weathercode",
            "snowfall"])
        return self