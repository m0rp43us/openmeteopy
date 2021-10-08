print(__name__)


from openmeteo_py.Hourly import Hourly 
from openmeteo_py.Daily import Daily 
from openmeteo_py.Options import Options
from openmeteo_py.OWmanager import OWmanager
# Latitude, Longitude for Rabat,Morocco
latitude = 33.9842
longitude = -6.8675

hourly = Hourly()
daily = Daily()
options = Options(latitude,longitude)

mgr = OWmanager(options,
    hourly.all(),
    daily.all())


# Download data
meteo = mgr.get_data()

print(meteo)