# Hourly updates & 1 km forecasts for Scandinavia


## Code Example :

```python 
from openmeteopy import OpenMeteo
from openmeteopy.hourly import HourlyMetno
from openmeteopy.options import MetnoOptions

# Latitude, Longitude for coordinates in Norway,any coordinates outside scandinavia will raise an error
longitude = 59.906296
latitude = 10.74408

hourly = HourlyMetno()
options = MetnoOptions(longitude,latitude)

mgr = OpenMeteo(options, hourly.temperature_2m())

# Download data
meteo = mgr.get_pandas()

print(meteo)
```


### Options :

|Parameter	            |Format	        |Required	|Default| 
|-----|--------|--------|--------|
|latitude, longitude	    | 	Floating point	|Yes|   - |
|elevation	            |String array 		|No|          auto
|timeformat	        | 	String	        |No|          iso8601|
|timezone    |String	        |No|           	GMT|
|past_days    |Integer (0-2)	        |No|           	0|
|start_end  |Boolean|No|False|
|start_date,end_date   |String (yyyy-mm-dd)	        |No|           	-|
|cell_selection   |String	        |No|           	nearest|
|current_weather   |Bool	        |No|           	false 	|
|temperature_unit   |String	        |No|           	celsius|
|windspeed_unit   |String	        |No|           	kmh|
|precipitation_unit   |String	        |No|           	mm|

### Hourly Parameter Definition :

|Variable                |Valid time|	            Unit|
|-----|----|-----|
|temperature_2m|	            Instant	 |               °C (°F)|
|relativehumidity_2m|	        Instant	  |              %|
|dewpoint_2m	       |         Instant	 |               °C (°F)|
|apparent_temperature	|    Instant	      |          °C (°F)|
|pressure_msl,surface_pressure	         |   Instant	       |         hPa|
|cloudcover	            |    Instant	      |          %|
|windspeed_10m              | Instant           |      km/h (mph, m/s, knots)|
|windgusts_10m	      |      Preceding hour max|	    km/h (mph, m/s)|
|winddirection_10m	      |Instant|	    °|
|shortwave_radiation	 |       Preceding hour mean	    W/m²|
|direct_radiation	      |  Preceding hour mean	|    W/m²|
|diffuse_radiation	     |   Preceding hour mean	|    W/mv²|
|vapor_pressure_deficit	  |  Instant	   |             kPa|
|precipitation	            |Preceding hour sum	|    mm (inch)|
|weathercode	               | Instant	  |              WMO code|
|et0_fao_evapotranspiration|	    Preceding hour sum	      |          mm (inch)|
|snowfall|	            Preceding hour sum	 |               cm (inch)|
|all|-|-|

