
class Daily():

    def __init__(self) :
        self.daily_params = []

    def temperature_2m_max(self):
        self.daily_params.append("temperature_2m_max")

    def temperature_2m_min(self):
        self.daily_params.append("temperature_2m_min")

    def apparent_temperature_max(self):
        self.daily_params.append("apparent_temperature_max")

    def apparent_temperature_min(self):
        self.daily_params.append("apparent_temperature_min")

    def precipitation_sum(self):
        self.daily_params.append("precipitation_sum")

    def precipitation_hours(self):
        self.daily_params.append("precipitation_hours")

    def weathercode(self):
        self.daily_params.append("weathercode")

    def sunrise(self):
        self.daily_params.append("sunrise")

    def sunset(self):
        self.daily_params.append("sunset")

    def windspeed_10m_max(self):
        self.daily_params.append("windspeed_10m_max")

    def windgusts_10m_max(self):
        self.daily_params.append("windgusts_10m_max")

    def winddirection_10m_dominant(self):
        self.daily_params.append("winddirection_10m_dominant")

    def shortwave_radiation_sum(self):
        self.daily_params.append("shortwave_radiation_sum")
