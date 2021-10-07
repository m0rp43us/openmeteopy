print(__name__)


from openmeteo_py import Hourly as h
from openmeteo_py import Daily as d
from openmeteo_py import Options as op
from openmeteo_py import OWmanager as ow
# Latitude, Longitude for Rabat,Morocco
latitude = 33.9842
longitude = -6.8675

hourly = h.Hourly()
daily = d.Daily()
options = op.Options(latitude,longitude)

mgr = ow.OWmanager(options,
    hourly.all(),
    daily.all())


# Download data
meteo = mgr.get_data()

print(meteo)