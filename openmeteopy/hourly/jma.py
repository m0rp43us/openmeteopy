from openmeteopy.hourly.meteo_france import HourlyMeteoFrance
from openmeteopy.exceptions import MethodnotAllowed

class HourlyJma(HourlyMeteoFrance):
    def windgusts_10m(self):
        """
        Overriding the windgust_10m method from HourlyMeteoFrance since it's not provided in Jma
        """

        raise MethodnotAllowed

    def all(self):
        """
        Overriding the all method from HourlyMeteoFrance since windgust_10m is not provided in Jma
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