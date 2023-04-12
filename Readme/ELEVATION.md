# 90 meter resolution digital elevation model

## Code Example 

```python

from openmeteo_py import OWmanager
from openmeteo_py.Options.ElevationOptions import ElevationOptions 

# Latitude, Longitude for Rabat,Morocco
latitude = 32.864823
longitude = -11.325094

options = ElevationOptions(longitude,latitude)

mgr = OWmanager(options,OWmanager.elevation
    )


# Download data
meteo = mgr.get_data()

print(meteo)

```

## Parameters


### Options :

|Parameter	            |Format	        |Required	|
|-----|----|-----|
|latitude|Floating point array|Geographical WGS84 coordinates of the location. Multiple coordinates can be coma , separated. Up to 100 coordinates can be requested at once.|
|longitude|Floating point array|Geographical WGS84 coordinates of the location. Multiple coordinates can be coma , separated. Up to 100 coordinates can be requested at once. |

