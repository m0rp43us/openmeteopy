from utils import *


class Hourly()  :

    def __init__(self) :
        self.hourly_params = TypedList()

    def temperature_2m(self):
        self.hourly_params.append("temperature_2m")
        return self

    def relativehumidity_2m(self):
        self.hourly_params.append("relativehumidity_2m")
        return self

    def dewpoint_2m(self):
        self.hourly_params.append("dewpoint_2m")
        return self

    def apparent_temperature(self):
        self.hourly_params.append("apparent_temperature")
        return self

    def pressure_msl(self):
        self.hourly_params.append("pressure_msl")
        return self

    def cloudcover(self):
        self.hourly_params.append("cloudcover")
        return self

    def cloudcover_low(self):
        self.hourly_params.append("cloudcover_low")
        return self

    def cloudcover_mid(self):
        self.hourly_params.append("cloudcover_mid")
        return self

    def cloudcover_high(self):
        self.hourly_params.append("cloudcover_high")
        return self

    def windspeed_10m(self):
        self.hourly_params.append("windspeed_10m")
        return self

    def windspeed_80m(self):
        self.hourly_params.append("windspeed_80m")
        return self

    def windspeed_120m(self):
        self.hourly_params.append("windspeed_120m")
        return self

    def windspeed_180m(self):
        self.hourly_params.append("windspeed_180m")
        return self

    def winddirection_10m(self):
        self.hourly_params.append("winddirection_10m")
        return self

    def winddirection_80m(self):
        self.hourly_params.append("winddirection_80m")
        return self

    def winddirection_120m(self):
        self.hourly_params.append("winddirection_120m")
        return self

    def winddirection_180m(self):
        self.hourly_params.append("winddirection_180m")
        return self

    def windgusts_10m(self):
        self.hourly_params.append("windgusts_10m")
        return self

    def shortwave_radiation(self):
        self.hourly_params.append("shortwave_radiation")
        return self

    def direct_radiation(self):
        self.hourly_params.append("irect_radiation")
        return self

    def diffuse_radiation(self):
        self.hourly_params.append("diffuse_radiation")
        return self

    def vapor_pressure_deficit(self):
        self.hourly_params.append("vapor_pressure_deficit")
        return self

    def evapotranspiration(self):
        self.hourly_params.append("evapotranspiration")
        return self

    def precipitation(self):
        self.hourly_params.append("precipitation")
        return self

    def weathercode(self):
        self.hourly_params.append("weathercode")
        return self

    def snow_height(self):
        self.hourly_params.append("snow_height")
        return self

    def freezinglevel_height(self):
        self.hourly_params.append("freezinglevel_height")
        return self

    def soil_temperature_0cm(self):
        self.hourly_params.append("soil_temperature_0cm")
        return self

    def soil_temperature_6cm(self):
        self.hourly_params.append("soil_temperature_6cm")
        return self

    def soil_temperature_18cm(self):
        self.hourly_params.append("soil_temperature_18cm")
        return self

    def soil_temperature_54cm(self):
        self.hourly_params.append("soil_temperature_54cm")
        return self

    def soil_moisture_0_1cm(self):
        self.hourly_params.append("soil_moisture_0_1cm")
        return self

    def soil_moisture_1_3cm(self):
        self.hourly_params.append("soil_moisture_1_3cm")
        return self

    def soil_moisture_3_9cm(self):
        self.hourly_params.append("soil_moisture_3_9cm")
        return self

    def soil_moisture_9_27cm(self):
        self.hourly_params.append("soil_moisture_9_27cm")
        return self

    def soil_moisture_27_81cm(self):
        self.hourly_params.append("soil_moisture_27_81cm")
        return self
    
    def all(self):
        self.hourly_params.append_all(["relativehumidity_2m",
            "dewpoint_2m",
            "apparent_temperature",
            "pressure_msl",
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
            "evapotranspiration",
            "precipitation",
            "weathercode",
            "snow_height",
            "freezinglevel_height",
            "soil_temperature_0cm",
            "soil_temperature_6cm",
            "soil_temperature_18cm",
            "soil_temperature_54cm",
            "soil_moisture_0_1cm",
            "soil_moisture_1_3cm",
            "soil_moisture_3_9cm",
            "soil_moisture_9_27cm",
            "soil_moisture_27_81cm"])
        return self




















