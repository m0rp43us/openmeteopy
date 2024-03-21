from openmeteopy.exceptions import *



class HourlyMeteoFrance()  :

    """
    hourly Parameter functions

    hourly Parameter Definition
    Most weather variables are given as an instantaneous value for the indicated hour. 
    Some variables like precipitation are calculated from the preceding hour as and average or sum.

    """


    def __init__(self) :
        self.hourly_params = TypedList()

    def temperature_2m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Air temperature at 2 meters above ground
        """

        self.hourly_params.append("temperature_2m")
        return self

    def relativehumidity_2m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`
        
        Relative humidity at 2 meters above ground
        
        """
        self.hourly_params.append("relativehumidity_2m")
        return self

    def dewpoint_2m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Dew point temperature at 2 meters above ground
        
        """

        self.hourly_params.append("dewpoint_2m")
        return self

    def apparent_temperature(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Apparent temperature is the perceived feels-like tempertature combinding wind chill factor, realtive humidity and solar radition

        
        """

        self.hourly_params.append("apparent_temperature")
        return self

    def pressure_msl(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Atmospheric air pressure reduced to sea level
        
        """

        self.hourly_params.append("pressure_msl")
        return self

    def cloudcover(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Total cloud cover as an area fraction
        
        """

        self.hourly_params.append("cloudcover")
        return self

    def cloudcover_low(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Low level clouds and fog up to 3 km altitude
        
        """

        self.hourly_params.append("cloudcover_low")
        return self

    def cloudcover_mid(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Mid level clouds from 3 to 8 km altitude

        
        """

        self.hourly_params.append("cloudcover_mid")
        return self

    def cloudcover_high(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        High level clouds from 8 km altitude
        
        """

        self.hourly_params.append("cloudcover_high")
        return self

    def windspeed_10m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Wind speed at 10 meters above ground. Wind speed on 10 meters is the standard level.

        
        """

        self.hourly_params.append("windspeed_10m")
        return self

    def winddirection_10m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Wind direction at 10 meters above ground
        """

        self.hourly_params.append("winddirection_10m")
        return self

    def windgusts_10m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Gusts at 10 meters above ground as a maximum of the preceding hour
        """

        self.hourly_params.append("windgusts_10m")
        return self

    def shortwave_radiation(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Shortwave solar radiation as average of the preceding hour
        """

        self.hourly_params.append("shortwave_radiation")
        return self

    def direct_radiation(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Direct solar radiation as average of the preceding hour
        """

        self.hourly_params.append("irect_radiation")
        return self

    def diffuse_radiation(self):
        """
        Returns the hourly configuration object
        :returns: `hourly()`

        Diffure solar radiation as average of the preceding hour
        """

        self.hourly_params.append("diffuse_radiation")
        return self

    def vapor_pressure_deficit(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Vapor Pressure Deificit (VPD) in kilo pascal (kPa). For high VPD (>1.6), water transpiration of plants increases. For low VPD (<0.4), transpiration decreases
        """

        self.hourly_params.append("vapor_pressure_deficit")
        return self

    def precipitation(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Total precipitation (rain, showers, snow) sum of the preceding hour
        """

        self.hourly_params.append("precipitation")
        return self

    def weathercode(self):
        """
        Returns the hourly configuration object
        :returns: `hourly()`

        Weather condition as a numeric code. Follow WMO weather interpretation codes. See table below for details.
        """

        self.hourly_params.append("weathercode")
        return self

    def snowfall(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7.
        """
        self.hourly_params.append("snowfall")
        return self
    
    def direct_normal_irradiance(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane.
        """
        self.hourly_params.append("direct_normal_irradiance")
        return self
    
    def cape(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Convective available potential energy.
        """
        self.hourly_params.append("cape")
        return self
    
    def et0_fao_evapotranspiration(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        ET₀ Reference Evapotranspiration of a well watered grass field. Based on FAO-56 Penman-Monteith equations ET₀ is calculated from temperature, wind speed, humidity and solar radiation. Unlimited soil water is assumed. ET₀ is commonly used to estimate the required irrigation for plants.
        """
        self.hourly_params.append("et0_fao_evapotranspiration")
        return self
    
    def surface_pressure(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation..
        """
        self.hourly_params.append("surface_pressure")
        return self
    
    def temperature_10hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 10hPa
        """
        self.hourly_params.append("temperature_10hPa")
        return self
    def temperature_20hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 20hPa
        """
        self.hourly_params.append("temperature_20hPa")
        return self
    def temperature_30hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 30hPa
        """
        self.hourly_params.append("temperature_30hPa")
        return self
    def temperature_50hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 50hPa
        """
        self.hourly_params.append("temperature_50hPa")
        return self
    def temperature_100hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 100hPa
        """
        self.hourly_params.append("temperature_100hPa")
        return self
    def temperature_150hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 150hPa
        """
        self.hourly_params.append("temperature_150hPa")
        return self
    def temperature_175hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 175hPa
        """
        self.hourly_params.append("temperature_175hPa")
        return self
    def temperature_200hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 200hPa
        """
        self.hourly_params.append("temperature_200hPa")
        return self
    def temperature_225hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 225hPa
        """
        self.hourly_params.append("temperature_225hPa")
        return self
    def temperature_250hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 250hPa
        """
        self.hourly_params.append("temperature_250hPa")
        return self
    def temperature_275hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 275hPa
        """
        self.hourly_params.append("temperature_275hPa")
        return self
    def temperature_300hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 300hPa
        """
        self.hourly_params.append("temperature_300hPa")
        return self
    def temperature_350hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 350hPa
        """
        self.hourly_params.append("temperature_350hPa")
        return self
    def temperature_400hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 400hPa
        """
        self.hourly_params.append("temperature_400hPa")
        return self
    def temperature_450hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 450hPa
        """
        self.hourly_params.append("temperature_450hPa")
        return self
    def temperature_500hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 500hPa
        """
        self.hourly_params.append("temperature_500hPa")
        return self
    def temperature_550hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 550hPa
        """
        self.hourly_params.append("temperature_550hPa")
        return self
    def temperature_600hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 600hPa
        """
        self.hourly_params.append("temperature_600hPa")
        return self
    def temperature_650hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 650hPa
        """
        self.hourly_params.append("temperature_650hPa")
        return self
    def temperature_700hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 700hPa
        """
        self.hourly_params.append("temperature_700hPa")
        return self
    def temperature_750hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 750hPa
        """
        self.hourly_params.append("temperature_750hPa")
        return self
    def temperature_800hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        temperature at 800hPa
        """
        self.hourly_params.append("temperature_800hPa")
        return self
    def dewpoint_10hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 10hPa
        """
        self.hourly_params.append("dewpoint_10hPa")
        return self
    def dewpoint_20hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 20hPa
        """
        self.hourly_params.append("dewpoint_20hPa")
        return self
    def dewpoint_30hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 30hPa
        """
        self.hourly_params.append("dewpoint_30hPa")
        return self
    def dewpoint_50hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 50hPa
        """
        self.hourly_params.append("dewpoint_50hPa")
        return self
    def dewpoint_100hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 100hPa
        """
        self.hourly_params.append("dewpoint_100hPa")
        return self
    def dewpoint_150hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 150hPa
        """
        self.hourly_params.append("dewpoint_150hPa")
        return self
    def dewpoint_175hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 175hPa
        """
        self.hourly_params.append("dewpoint_175hPa")
        return self
    def dewpoint_200hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 200hPa
        """
        self.hourly_params.append("dewpoint_200hPa")
        return self
    def dewpoint_225hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 225hPa
        """
        self.hourly_params.append("dewpoint_225hPa")
        return self
    def dewpoint_250hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 250hPa
        """
        self.hourly_params.append("dewpoint_250hPa")
        return self
    def dewpoint_275hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 275hPa
        """
        self.hourly_params.append("dewpoint_275hPa")
        return self
    def dewpoint_300hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 300hPa
        """
        self.hourly_params.append("dewpoint_300hPa")
        return self
    def dewpoint_350hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 350hPa
        """
        self.hourly_params.append("dewpoint_350hPa")
        return self
    def dewpoint_400hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 400hPa
        """
        self.hourly_params.append("dewpoint_400hPa")
        return self
    def dewpoint_450hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 450hPa
        """
        self.hourly_params.append("dewpoint_450hPa")
        return self
    def dewpoint_500hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 500hPa
        """
        self.hourly_params.append("dewpoint_500hPa")
        return self
    def dewpoint_550hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 550hPa
        """
        self.hourly_params.append("dewpoint_550hPa")
        return self
    def dewpoint_600hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 600hPa
        """
        self.hourly_params.append("dewpoint_600hPa")
        return self
    def dewpoint_650hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 650hPa
        """
        self.hourly_params.append("dewpoint_650hPa")
        return self
    def dewpoint_700hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 700hPa
        """
        self.hourly_params.append("dewpoint_700hPa")
        return self
    def dewpoint_750hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 750hPa
        """
        self.hourly_params.append("dewpoint_750hPa")
        return self
    def dewpoint_800hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        dewpoint at 800hPa
        """
        self.hourly_params.append("dewpoint_800hPa")
        return self
    def relativehumidity_10hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 10hPa
        """
        self.hourly_params.append("relativehumidity_10hPa")
        return self
    def relativehumidity_20hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 20hPa
        """
        self.hourly_params.append("relativehumidity_20hPa")
        return self
    def relativehumidity_30hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 30hPa
        """
        self.hourly_params.append("relativehumidity_30hPa")
        return self
    def relativehumidity_50hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 50hPa
        """
        self.hourly_params.append("relativehumidity_50hPa")
        return self
    def relativehumidity_100hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 100hPa
        """
        self.hourly_params.append("relativehumidity_100hPa")
        return self
    def relativehumidity_150hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 150hPa
        """
        self.hourly_params.append("relativehumidity_150hPa")
        return self
    def relativehumidity_175hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 175hPa
        """
        self.hourly_params.append("relativehumidity_175hPa")
        return self
    def relativehumidity_200hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 200hPa
        """
        self.hourly_params.append("relativehumidity_200hPa")
        return self
    def relativehumidity_225hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 225hPa
        """
        self.hourly_params.append("relativehumidity_225hPa")
        return self
    def relativehumidity_250hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 250hPa
        """
        self.hourly_params.append("relativehumidity_250hPa")
        return self
    def relativehumidity_275hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 275hPa
        """
        self.hourly_params.append("relativehumidity_275hPa")
        return self
    def relativehumidity_300hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 300hPa
        """
        self.hourly_params.append("relativehumidity_300hPa")
        return self
    def relativehumidity_350hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 350hPa
        """
        self.hourly_params.append("relativehumidity_350hPa")
        return self
    def relativehumidity_400hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 400hPa
        """
        self.hourly_params.append("relativehumidity_400hPa")
        return self
    def relativehumidity_450hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 450hPa
        """
        self.hourly_params.append("relativehumidity_450hPa")
        return self
    def relativehumidity_500hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 500hPa
        """
        self.hourly_params.append("relativehumidity_500hPa")
        return self
    def relativehumidity_550hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 550hPa
        """
        self.hourly_params.append("relativehumidity_550hPa")
        return self
    def relativehumidity_600hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 600hPa
        """
        self.hourly_params.append("relativehumidity_600hPa")
        return self
    def relativehumidity_650hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 650hPa
        """
        self.hourly_params.append("relativehumidity_650hPa")
        return self
    def relativehumidity_700hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 700hPa
        """
        self.hourly_params.append("relativehumidity_700hPa")
        return self
    def relativehumidity_750hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 750hPa
        """
        self.hourly_params.append("relativehumidity_750hPa")
        return self
    def relativehumidity_800hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        relativehumidity at 800hPa
        """
        self.hourly_params.append("relativehumidity_800hPa")
        return self
    def cloudcover_10hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 10hPa
        """
        self.hourly_params.append("cloudcover_10hPa")
        return self
    def cloudcover_20hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 20hPa
        """
        self.hourly_params.append("cloudcover_20hPa")
        return self
    def cloudcover_30hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 30hPa
        """
        self.hourly_params.append("cloudcover_30hPa")
        return self
    def cloudcover_50hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 50hPa
        """
        self.hourly_params.append("cloudcover_50hPa")
        return self
    def cloudcover_100hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 100hPa
        """
        self.hourly_params.append("cloudcover_100hPa")
        return self
    def cloudcover_150hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 150hPa
        """
        self.hourly_params.append("cloudcover_150hPa")
        return self
    def cloudcover_175hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 175hPa
        """
        self.hourly_params.append("cloudcover_175hPa")
        return self
    def cloudcover_200hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 200hPa
        """
        self.hourly_params.append("cloudcover_200hPa")
        return self
    def cloudcover_225hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 225hPa
        """
        self.hourly_params.append("cloudcover_225hPa")
        return self
    def cloudcover_250hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 250hPa
        """
        self.hourly_params.append("cloudcover_250hPa")
        return self
    def cloudcover_275hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 275hPa
        """
        self.hourly_params.append("cloudcover_275hPa")
        return self
    def cloudcover_300hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 300hPa
        """
        self.hourly_params.append("cloudcover_300hPa")
        return self
    def cloudcover_350hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 350hPa
        """
        self.hourly_params.append("cloudcover_350hPa")
        return self
    def cloudcover_400hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 400hPa
        """
        self.hourly_params.append("cloudcover_400hPa")
        return self
    def cloudcover_450hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 450hPa
        """
        self.hourly_params.append("cloudcover_450hPa")
        return self
    def cloudcover_500hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 500hPa
        """
        self.hourly_params.append("cloudcover_500hPa")
        return self
    def cloudcover_550hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 550hPa
        """
        self.hourly_params.append("cloudcover_550hPa")
        return self
    def cloudcover_600hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 600hPa
        """
        self.hourly_params.append("cloudcover_600hPa")
        return self
    def cloudcover_650hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 650hPa
        """
        self.hourly_params.append("cloudcover_650hPa")
        return self
    def cloudcover_700hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 700hPa
        """
        self.hourly_params.append("cloudcover_700hPa")
        return self
    def cloudcover_750hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 750hPa
        """
        self.hourly_params.append("cloudcover_750hPa")
        return self
    def cloudcover_800hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        cloudcover at 800hPa
        """
        self.hourly_params.append("cloudcover_800hPa")
        return self
    def windspeed_10hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 10hPa
        """
        self.hourly_params.append("windspeed_10hPa")
        return self
    def windspeed_20hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 20hPa
        """
        self.hourly_params.append("windspeed_20hPa")
        return self
    def windspeed_30hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 30hPa
        """
        self.hourly_params.append("windspeed_30hPa")
        return self
    def windspeed_50hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 50hPa
        """
        self.hourly_params.append("windspeed_50hPa")
        return self
    def windspeed_100hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 100hPa
        """
        self.hourly_params.append("windspeed_100hPa")
        return self
    def windspeed_150hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 150hPa
        """
        self.hourly_params.append("windspeed_150hPa")
        return self
    def windspeed_175hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 175hPa
        """
        self.hourly_params.append("windspeed_175hPa")
        return self
    def windspeed_200hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 200hPa
        """
        self.hourly_params.append("windspeed_200hPa")
        return self
    def windspeed_225hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 225hPa
        """
        self.hourly_params.append("windspeed_225hPa")
        return self
    def windspeed_250hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 250hPa
        """
        self.hourly_params.append("windspeed_250hPa")
        return self
    def windspeed_275hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 275hPa
        """
        self.hourly_params.append("windspeed_275hPa")
        return self
    def windspeed_300hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 300hPa
        """
        self.hourly_params.append("windspeed_300hPa")
        return self
    def windspeed_350hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 350hPa
        """
        self.hourly_params.append("windspeed_350hPa")
        return self
    def windspeed_400hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 400hPa
        """
        self.hourly_params.append("windspeed_400hPa")
        return self
    def windspeed_450hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 450hPa
        """
        self.hourly_params.append("windspeed_450hPa")
        return self
    def windspeed_500hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 500hPa
        """
        self.hourly_params.append("windspeed_500hPa")
        return self
    def windspeed_550hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 550hPa
        """
        self.hourly_params.append("windspeed_550hPa")
        return self
    def windspeed_600hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 600hPa
        """
        self.hourly_params.append("windspeed_600hPa")
        return self
    def windspeed_650hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 650hPa
        """
        self.hourly_params.append("windspeed_650hPa")
        return self
    def windspeed_700hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 700hPa
        """
        self.hourly_params.append("windspeed_700hPa")
        return self
    def windspeed_750hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 750hPa
        """
        self.hourly_params.append("windspeed_750hPa")
        return self
    def windspeed_800hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        windspeed at 800hPa
        """
        self.hourly_params.append("windspeed_800hPa")
        return self
    def winddirection_10hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 10hPa
        """
        self.hourly_params.append("winddirection_10hPa")
        return self
    def winddirection_20hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 20hPa
        """
        self.hourly_params.append("winddirection_20hPa")
        return self
    def winddirection_30hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 30hPa
        """
        self.hourly_params.append("winddirection_30hPa")
        return self
    def winddirection_50hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 50hPa
        """
        self.hourly_params.append("winddirection_50hPa")
        return self
    def winddirection_100hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 100hPa
        """
        self.hourly_params.append("winddirection_100hPa")
        return self
    def winddirection_150hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 150hPa
        """
        self.hourly_params.append("winddirection_150hPa")
        return self
    def winddirection_175hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 175hPa
        """
        self.hourly_params.append("winddirection_175hPa")
        return self
    def winddirection_200hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 200hPa
        """
        self.hourly_params.append("winddirection_200hPa")
        return self
    def winddirection_225hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 225hPa
        """
        self.hourly_params.append("winddirection_225hPa")
        return self
    def winddirection_250hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 250hPa
        """
        self.hourly_params.append("winddirection_250hPa")
        return self
    def winddirection_275hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 275hPa
        """
        self.hourly_params.append("winddirection_275hPa")
        return self
    def winddirection_300hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 300hPa
        """
        self.hourly_params.append("winddirection_300hPa")
        return self
    def winddirection_350hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 350hPa
        """
        self.hourly_params.append("winddirection_350hPa")
        return self
    def winddirection_400hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 400hPa
        """
        self.hourly_params.append("winddirection_400hPa")
        return self
    def winddirection_450hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 450hPa
        """
        self.hourly_params.append("winddirection_450hPa")
        return self
    def winddirection_500hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 500hPa
        """
        self.hourly_params.append("winddirection_500hPa")
        return self
    def winddirection_550hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 550hPa
        """
        self.hourly_params.append("winddirection_550hPa")
        return self
    def winddirection_600hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 600hPa
        """
        self.hourly_params.append("winddirection_600hPa")
        return self
    def winddirection_650hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 650hPa
        """
        self.hourly_params.append("winddirection_650hPa")
        return self
    def winddirection_700hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 700hPa
        """
        self.hourly_params.append("winddirection_700hPa")
        return self
    def winddirection_750hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 750hPa
        """
        self.hourly_params.append("winddirection_750hPa")
        return self
    def winddirection_800hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        winddirection at 800hPa
        """
        self.hourly_params.append("winddirection_800hPa")
        return self
    def geopotential_height_10hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 10hPa
        """
        self.hourly_params.append("geopotential_height_10hPa")
        return self
    def geopotential_height_20hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 20hPa
        """
        self.hourly_params.append("geopotential_height_20hPa")
        return self
    def geopotential_height_30hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 30hPa
        """
        self.hourly_params.append("geopotential_height_30hPa")
        return self
    def geopotential_height_50hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 50hPa
        """
        self.hourly_params.append("geopotential_height_50hPa")
        return self
    def geopotential_height_100hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 100hPa
        """
        self.hourly_params.append("geopotential_height_100hPa")
        return self
    def geopotential_height_150hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 150hPa
        """
        self.hourly_params.append("geopotential_height_150hPa")
        return self
    def geopotential_height_175hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 175hPa
        """
        self.hourly_params.append("geopotential_height_175hPa")
        return self
    def geopotential_height_200hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 200hPa
        """
        self.hourly_params.append("geopotential_height_200hPa")
        return self
    def geopotential_height_225hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 225hPa
        """
        self.hourly_params.append("geopotential_height_225hPa")
        return self
    def geopotential_height_250hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 250hPa
        """
        self.hourly_params.append("geopotential_height_250hPa")
        return self
    def geopotential_height_275hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 275hPa
        """
        self.hourly_params.append("geopotential_height_275hPa")
        return self
    def geopotential_height_300hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 300hPa
        """
        self.hourly_params.append("geopotential_height_300hPa")
        return self
    def geopotential_height_350hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 350hPa
        """
        self.hourly_params.append("geopotential_height_350hPa")
        return self
    def geopotential_height_400hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 400hPa
        """
        self.hourly_params.append("geopotential_height_400hPa")
        return self
    def geopotential_height_450hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 450hPa
        """
        self.hourly_params.append("geopotential_height_450hPa")
        return self
    def geopotential_height_500hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 500hPa
        """
        self.hourly_params.append("geopotential_height_500hPa")
        return self
    def geopotential_height_550hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 550hPa
        """
        self.hourly_params.append("geopotential_height_550hPa")
        return self
    def geopotential_height_600hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 600hPa
        """
        self.hourly_params.append("geopotential_height_600hPa")
        return self
    def geopotential_height_650hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 650hPa
        """
        self.hourly_params.append("geopotential_height_650hPa")
        return self
    def geopotential_height_700hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 700hPa
        """
        self.hourly_params.append("geopotential_height_700hPa")
        return self
    def geopotential_height_750hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 750hPa
        """
        self.hourly_params.append("geopotential_height_750hPa")
        return self
    def geopotential_height_800hpa(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()` 
        geopotential_height at 800hPa
        """
        self.hourly_params.append("geopotential_height_800hPa")
        return self

    def all(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

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
            "cloudcover_low",
            "cloudcover_mid",
            "cloudcover_high",
            "windspeed_10m",
            "winddirection_10m",
            "windgusts_10m",
            "shortwave_radiation",
            "direct_radiation",
            "diffuse_radiation",
            "vapor_pressure_deficit",
            "cape",
            "et0_fao_evapotranspiration",
            "precipitation",
            "weathercode",
            "snowfall"
            ])
        return self