from openmeteopy.utils.constants import *
from openmeteopy.utils.timezones import *
from openmeteopy.options.forecast import ForecastOptions


class MarineOptions(ForecastOptions):
    API_PATH = "https://marine-api.open-meteo.com/v1/marine?"

    def get_api_path(self):
        return self.API_PATH

    pass
