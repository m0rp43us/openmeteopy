from openmeteopy.options.meteo_france import MeteoFranceOptions

class DwdOptions(MeteoFranceOptions):
    API_PATH = "https://api.open-meteo.com/v1/dwd-icon?"

    def get_api_path(self):
        return self.API_PATH

    pass