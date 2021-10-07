from utils import *

class Daily():

    def __init__(self) :
        self.daily_params = TypedList()

    def temperature_2m_max(self):
        self.daily_params.append("temperature_2m_max")
        return self

    def temperature_2m_min(self):
        self.daily_params.append("temperature_2m_min")
        return self

    def apparent_temperature_max(self):
        self.daily_params.append("apparent_temperature_max")
        return self

    def apparent_temperature_min(self):
        self.daily_params.append("apparent_temperature_min")
        return self

    def precipitation_sum(self):
        self.daily_params.append("precipitation_sum")
        return self

    def precipitation_hours(self):
        self.daily_params.append("precipitation_hours")
        return self

    def weathercode(self):
        self.daily_params.append("weathercode")
        return self

    def sunrise(self):
        self.daily_params.append("sunrise")
        return self

    def sunset(self):
        self.daily_params.append("sunset")
        return self

    def windspeed_10m_max(self):
        self.daily_params.append("windspeed_10m_max")
        return self

    def windgusts_10m_max(self):
        self.daily_params.append("windgusts_10m_max")
        return self

    def winddirection_10m_dominant(self):
        self.daily_params.append("winddirection_10m_dominant")
        return self

    def shortwave_radiation_sum(self):
        self.daily_params.append("shortwave_radiation_sum")
        return self
    
    def all(self):
        self.daily_params.append_all(["temperature_2m_max",                                                                             
            "temperature_2m_min",
            "apparent_temperature_max",
            "apparent_temperature_min",
            "precipitation_sum",
            "precipitation_hours",
            "weathercode",
            "sunrise",
            "sunset",
            "windspeed_10m_max",
            "windgusts_10m_max",
            "winddirection_10m_dominant",
            "shortwave_radiation_sum"])
        return self




