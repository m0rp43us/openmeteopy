# Hourly and daily wave forecasts at 5 km resolution

## Code Example :

```python 
from openmeteopy import OWmanager
from openmeteopy.hourly import HourlyMarine
from openmeteopy.options import MarineOptions

# Latitude, Longitude 
longitude = 59.906296
latitude = 10.74408

hourly = HourlyMarine()
options = MarineOptions(longitude,latitude)

mgr = OpenMeteo(options, hourly.swell_wave_height())

# Download data
meteo = mgr.get_pandas()

print(meteo)
```


## Options :

|Parameter	            |Format	        |Required	|Default|
|-----|--------|--------|--------|
|latitude, longitude	    |Floating point	|Yes|    -    |
|timeformat	            |String	        |No|          iso8601|
|timezone	            |String	        |No|	        UTC|
|past_days	            |Integer (0-2)	|No|          0|
|start_end  |Boolean|No|False|
|start_date        |String (yyyy-mm-dd)|No|          -|
|end_date	    |String (yyyy-mm-dd)|No|          -|
|cell_selection |String	        |No|sea|

## Hourly Parameter Definition :

|Variable                |Valid time|	            Unit|
|-----|----|-----|
|wave_height|	            Instant	 |               Meter|
|wind_wave_height|	        Instant	  |              Meter|
|swell_wave_height|         Instant	 |               Meter|
|wave_direction|    Instant	      |          °|
|wind_wave_direction|   Instant	       |         °|
|swell_wave_direction|    Instant	      |          °|
|wave_period|   Instant	        |        Seconds|
|wind_wave_period|  Instant	       |        Seconds|
|swell_wave_period|   Instant	       |         Seconds|
|wind_wave_peak_period| Instant           |      Seconds|
|swell_wave_peak_period|               Instant            |     Seconds|

## Daily Parameter Definition

|Variable	        |            Unit|
|----|------|
|wave_height_max| Meter|
|wind_wave_height_max| Meter|
|swell_wave_height_max|   Meter|
|wave_direction_dominant|  °|
|wind_wave_direction_dominant |     °|
|swell_wave_direction_dominant|  °|
|wave_period_max|   Seconds|
|wind_wave_period_max|   Seconds|
|swell_wave_period_max|   Seconds|
|wind_wave_peak_period_max|Seconds|
|swell_wave_peak_period_max|Seconds|

