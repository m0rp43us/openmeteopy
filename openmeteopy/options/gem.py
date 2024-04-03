from openmeteopy.utils.constants import *
from openmeteopy.utils.timezones import *
from openmeteopy.options.forecast import ForecastOptions


class GemOptions(ForecastOptions):
    API_PATH = "https://api.open-meteo.com/v1/gem?"

    def get_api_path(self):
        return self.API_PATH

    pass