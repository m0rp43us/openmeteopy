# Simulated river discharge at 5 km resolution from 1984 up to 7 months forecast


### Code Example :

```python 
from openmeteopy import OpenMeteo
from openmeteopy.daily import DailyFlood
from openmeteopy.options import FloodOptions

# Latitude, Longitude 
longitude = 59.906296
latitude = 10.74408

daily = DailyFlood()
options = FloodOptions(longitude,latitude)

mgr = OpenMeteo(options, daily=daily.all())

# Download data
meteo = mgr.get_pandas()

print(meteo)
```


### Options :

|Parameter	            |Format	        |Required	|Default| 
|-----|--------|--------|--------|
|latitude, longitude	    | 	Floating point	|Yes|   - |
|forecast_days	            |Integer (0-16)		|No|          92|
|timeformat	        | 	String	        |No|          iso8601|
|past_days    |Integer (0-2)	        |No|           	0|
|start_end  |Boolean|No|False|
|start_date,end_date   |String (yyyy-mm-dd)	        |No|           	-|
|ensemble   |Boolean	        |No|           	-|
|cell_selection   |String	        |No|           	nearest|

### Hourly Parameter Definition :

|Variable                |	            Unit|
|-----|-----|
|river_discharge_mean|                	m³/s|
|river_discharge_median|	                   m³/s|
|river_discharge_max|            m³/s|
|river_discharge_min|            m³/s|
|river_discharge_p25|    m³/s|
|river_discharge_p75|                m³/s|
