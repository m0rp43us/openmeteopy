from openmeteo_py.Daily.DailyMeteoFrance import DailyMeteoFrance
from openmeteo_py.Exceptions import MethodnotAllowed


class DailyJma(DailyMeteoFrance):

    def windgusts_10m_max(self):
        """
        Overriding the windgust_10m_max method from HourlyMeteoFrance since it's not provided in Jma
        """
        raise MethodnotAllowed

    def all(self):
        """
        Overriding the all method from HourlyMeteoFrance since windgust_10m_max is not provided in Jma
        """
        self.daily_params.append_all([
            "temperature_2m_max",                                                                             
            "temperature_2m_min",
            "apparent_temperature_max",
            "apparent_temperature_min",
            "precipitation_sum",
            "precipitation_hours",
            "sunrise",
            "snowfall_sum",
            "sunset",
            "windspeed_10m_max",
            "winddirection_10m_dominant",
            "shortwave_radiation_sum",
            "et0_fao_evapotranspiration"])
        return self