# 90 meter resolution digital elevation model

## Code Example 

```python
from openmeteopy import OpenMeteo
from openmeteopy.options import ElevationOptions 

# Latitude, Longitude for Rabat,Morocco
latitude = 32.864823
longitude = -11.325094

options = ElevationOptions(longitude,latitude)

mgr = OpenMeteo(options)

# Download data
meteo = mgr.get_pandas()

print(meteo)
```

## Parameters


### Options :

|Parameter	            |Format	        |Required	|
|-----|----|-----|
|latitude|Floating point array|Geographical WGS84 coordinates of the location. Multiple coordinates can be coma , separated. Up to 100 coordinates can be requested at once.|
|longitude|Floating point array|Geographical WGS84 coordinates of the location. Multiple coordinates can be coma , separated. Up to 100 coordinates can be requested at once. |

