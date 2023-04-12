# Simulated river discharge at 5 km resolution from 1984 up to 7 months forecast


### Code Example :

```python 

#from openmeteo_py.Daily.Marine import Marine as Daily
from openmeteo_py import OWmanager
from openmeteo_py.Daily.DailyFlood import DailyFlood
from openmeteo_py.Options.FloodOptions import FloodOptions

# Latitude, Longitude 
longitude = 	59.906296
latitude = 10.74408

daily = DailyFlood()
options = FloodOptions(longitude,latitude)

#notice that we had to give the value "None" for the hourly parameter,otherwise you'll be filling the hourly parameter instead of the daily one,which will raise an error.
mgr = OWmanager(options,OWmanager.flood,None,daily.all())


# Download data
meteo = mgr.get_data()

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
