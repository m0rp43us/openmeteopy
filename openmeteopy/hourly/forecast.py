from openmeteopy.exceptions import *

class HourlyForecast():

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

    def windspeed_80m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Wind speed at 80 meters above ground. Wind speed on 10 meters is the standard level.
        
        """

        self.hourly_params.append("windspeed_80m")
        return self

    def windspeed_120m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Wind speed at 120 meters above ground. Wind speed on 10 meters is the standard level.
        """

        self.hourly_params.append("windspeed_120m")
        return self

    def windspeed_180m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Wind speed at 180 meters above ground. Wind speed on 10 meters is the standard level.
        """

        self.hourly_params.append("windspeed_180m")
        return self

    def winddirection_10m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Wind direction at 10 meters above ground
        """

        self.hourly_params.append("winddirection_10m")
        return self

    def winddirection_80m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Wind direction at 80 meters above ground
        """

        self.hourly_params.append("winddirection_80m")
        return self

    def winddirection_120m(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Wind direction at 120 meters above ground
        """

        self.hourly_params.append("winddirection_120m")
        return self

    def winddirection_180m(self):
        """
        Returns the hourly configuration object
        :returns: `hourly()`

        Wind direction at 180 meters above ground
        """

        self.hourly_params.append("winddirection_180m")
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

    def evapotranspiration(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Sum of evapotranspration of the preceding hour from lands urface and plants
        """

        self.hourly_params.append("evapotranspiration")
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

    def snow_depth(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Snow depth on the ground
        """

        self.hourly_params.append("snow_height")
        return self

    def freezinglevel_height(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Altitude of the 0°C level
        """

        self.hourly_params.append("freezinglevel_height")
        return self

    def soil_temperature_0cm(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Temperature in the soil at 0 cm depths. 0 cm is the surface temperature on land or water surface temperature on water.
        """

        self.hourly_params.append("soil_temperature_0cm")
        return self

    def soil_temperature_6cm(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Temperature in the soil at  6 cm depths.
        """
        self.hourly_params.append("soil_temperature_6cm")
        return self

    def soil_temperature_18cm(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Temperature in the soil at  18 cm depths.
        """
        self.hourly_params.append("soil_temperature_18cm")
        return self

    def soil_temperature_54cm(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Temperature in the soil at  54 cm depths.
        """
        self.hourly_params.append("soil_temperature_54cm")
        return self

    def soil_moisture_0_1cm(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Average soil water content as volumetric mixing ratio at 0-1 cm depths.
        """
        self.hourly_params.append("soil_moisture_0_1cm")
        return self

    def soil_moisture_1_3cm(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Average soil water content as volumetric mixing ratio at 1-3 cm depths.
        """
        self.hourly_params.append("soil_moisture_1_3cm")
        return self

    def soil_moisture_3_9cm(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Average soil water content as volumetric mixing ratio at 3-9 cm depths.
        """
        self.hourly_params.append("soil_moisture_3_9cm")
        return self

    def soil_moisture_9_27cm(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Average soil water content as volumetric mixing ratio at 9-27 cm depths.
        """
        self.hourly_params.append("soil_moisture_9_27cm")
        return self

    def Showers(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Average soil water content as volumetric mixing ratio at 27-81 cm depths.
        """
        self.hourly_params.append("showers")
        return self
    
    def snowfall(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7.
        """
        self.hourly_params.append("snowfall")
        return self
    
    def soil_moisture_27_81cm(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Average soil water content as volumetric mixing ratio at 27-81 cm depths.
        """
        self.hourly_params.append("soil_moisture_27_81cm")
        return self
    
    def visibility(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Viewing distance in meters. Influenced by low clouds, humidity and aerosols. Maximum visibility is approximately 24 km.
        """
        self.hourly_params.append("visibility")
        return self
    
    def direct_normal_irradiance(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane.
        """
        self.hourly_params.append("direct_normal_irradiance")
        return self
    
    def direct_radiation(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Direct solar radiation as average of the preceding hour on the horizontal plane and the normal plane.
        """
        self.hourly_params.append("direct_radiation")
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
    
    def is_day(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        1 if the current time step has daylight, 0 at night..
        """
        self.hourly_params.append("soil_moisture_27_81cm")
        return self
    
    def rain(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Rain from large scale weather systems of the preceding hour in millimeter.
        """
        self.hourly_params.append("rain")
        return self
    
    def surface_pressure(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Atmospheric air pressure reduced to mean sea level (msl) or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation..
        """
        self.hourly_params.append("surface_pressure")
        return self
    
    def precipitation_probability(self):
        """
        Returns the hourly configuration object 
        :returns: `hourly()`

        Probability of precipitation with more than 0.1 mm of the preceding hour. Probability is based on ensemble weather models with 0.25° (~27 km) resolution. 30 different simulations are computed to better represent future weather conditions.
        """
        self.hourly_params.append("precipitation_probability")
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
            "windspeed_80m",
            "windspeed_120m",
            "windspeed_180m",
            "winddirection_10m",
            "winddirection_80m",
            "winddirection_120m",
            "winddirection_180m",
            "windgusts_10m",
            "shortwave_radiation",
            "direct_radiation",
            "diffuse_radiation",
            "vapor_pressure_deficit",
            "cape",
            "evapotranspiration",
            "et0_fao_evapotranspiration",
            "precipitation",
            "weathercode",
            "snow_depth",
            "showers",
            "snowfall",
            "visibility",
            "precipitation_probability",
            "freezinglevel_height",
            "soil_temperature_0cm",
            "soil_temperature_6cm",
            "soil_temperature_18cm",
            "soil_temperature_54cm",
            "soil_moisture_0_1cm",
            "soil_moisture_1_3cm",
            "soil_moisture_3_9cm",
            "soil_moisture_9_27cm",
            "soil_moisture_27_81cm",
            "is_day"])
        return self