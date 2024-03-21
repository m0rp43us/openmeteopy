# 2.5 km high resolution forecasts for North America

## Code Example :

```python
from openmeteopy import OpenMeteo
from openmeteopy.hourly import HourlyGem
from openmeteopy.options import GemOptions
from openmeteopy.utils.constants import *

# Latitude, Longitude 
longitude = 33.89
latitude =  -6.31

hourly = HourlyGem()
options = GemOptions(latitude,longitude)

mgr = OpenMeteo(options, hourly.cloudcover_150hpa())

# Download data
meteo = mgr.get_pandas()

print(meteo)
```

## Parameters:


### Options:

|Parameter	            |Format	        |Required	|Default|
|-----|--------|--------|--------|
|latitude, longitude	    |Floating point	|Yes|        |
|elevation	            |Floating point	|No|          0|
|current_weather	        |Bool	        |No|          false|
|temperature_unit	    |String	        |No|          celsius|
|windspeed_unit	        |String	        |No|          kmh|
|precipitation_unit	    |String          |No|         kmh|
|timeformat	            |String	        |No|          iso8601|
|timezone	            |String	        |No|	        UTC|
|past_days	            |Integer (0-2)	|No|          0|
|start_end  |Boolean|No|False|
|start_date	            |String (yyyy-mm-dd)	|No|          -|
|end_date	            |String (yyyy-mm-dd)	|No|          -|
|cell_selection	            |String	|No|          land|

### Hourly Parameter Definition:

|Variable                |Valid time|	            Unit|
|-----|----|-----|
|temperature_2m|	            Instant	 |               °C (°F)|
|temperature_40m|	            Instant	 |               °C (°F)|
|temperature_80m|	            Instant	 |               °C (°F)|
|temperature_120m|	            Instant	 |               °C (°F)|
|relativehumidity_2m|	        Instant	  |              %|
|dewpoint_2m	       |         Instant	 |               °C (°F)|
|apparent_temperature	|    Instant	      |          °C (°F)|
|pressure_msl,surface_pressure	         |   Instant	       |         hPa|
|cloudcover	            |    Instant	      |          %|
|cloudcover_low	         |   Instant	        |        %|
|cloudcover_mid	          |  Instant	       |        %|
|cloudcover_high	         |   Instant	       |         %|
|windspeed_10m              | Instant           |      km/h (mph, m/s, knots)|
|windspeed_80m|               Instant            |     km/h (mph, m/s, knots)|
|windspeed_120m|              Instant             |  km/h (mph, m/s, knots)|
|windspeed_180m	|            Instant	             |   km/h (mph, m/s, knots)|
|winddirection_10m|           Instant|                 °|
|winddirection_80m |          Instant |                °|
|winddirection_120m |         Instant  |               °|
|winddirection_180m	 |       Instant	  |              °|
|windgusts_10m	      |      Preceding hour max|	    km/h (mph, m/s)|
|shortwave_radiation	 |       Preceding hour mean	    W/m²|
|direct_radiation	      |  Preceding hour mean	|    W/m²|
|diffuse_radiation	     |   Preceding hour mean	|    W/mv²|
|vapor_pressure_deficit	  |  Instant	   |             kPa|
|evapotranspiration	       | Preceding hour sum|	    mm (inch)|
|precipitation	            |Preceding hour sum	|    mm (inch)|
|weathercode	               | Instant	  |              WMO code|
|snow_depth	                |Instant	|                meters|
|freezinglevel_height|	    Instant	     |           meters|
|soil_temperature_0_to_10cm |       Instant |                °C (°F)|
|soil_moisture_0_to_10cm  |      Instant     |            °C (°F)|
|all|-|-|

### Daily Parameter Definition:

|Variable	        |            Unit|
|----|------|
|temperature_2m_max            |  °C (°F)|
|temperature_2m_min	          |  °C (°F)|
|apparent_temperature_max    |    °C (°F)|
|apparent_temperature_min	  |  °C (°F)|
|precipitation_sum	       |     mm|
|precipitation_hours	          |  hours|
|weathercode	                 |   WMO code|
|sunrise                      |   iso8601|
|sunset	                     |   iso8601|
|windspeed_10m_max|km/h (mph, m/s, knots)|
|windgusts_10m_max	        |    km/h (mph, m/s, knots)|
|winddirection_10m_dominant|	    °|
|shortwave_radiation_sum|	        MJ/m²|
|all|-|


### Pressure Level Variables:

Pressure level variables do not have fixed altitudes. Altitude varies with atmospheric pressure. 1000 hPa is roughly between 60 and 160 meters above sea level. Estimated altitudes are given below. Altitudes are in meters above sea level (not above ground). For precise altitudes, geopotential_height can be used.
|Variable     |   Unit|
|------|-------|
|weathercode|	            WMO code|
|temperature_1015hPa ... temperature_10hPa|	        °C (°F)|
|relativehumidity_1015hPa ... relativehumidity_10hPa	 |       %|
|dewpoint_1015hPa ... dewpoint_10hPa |	    °C (°F)|
|cloudcover_1015hPa ... cloudcover_10hPa   |    %|
|windspeed_1015hPa	... windspeed_10hPa |   km/h (mph, m/s, knots)|
|winddirection_1015hPa	...  winddirection_10hPa   |    °|
|geopotential_height_1015hPa ... geopotential_height_10hPa	 |   meter|

### Pressure level methods:

to call a pressure level method all you have to do is put the variable for example ; ``` temperature ``` then an underscore ``` _ ``` and the equivalent pressure level for example : ``` 1015hpa  ```

for this example the method is ``` temperature_1015hpa() ``` 

### pressure - elevation equivalent

|Pressure     |   Elevation|
|------|-------|
|10 hPa |26 km|
|20 hPa |23 km|
|30 hPa |22 km|
|50 hPa |19.3 km|
|100 hPa |15.8 km|
|150 hPa |13.5 km|
|175 hPa |12.6 km|
|200 hPa |11.8 km|
|225 hPa |11 km|
|250 hPa |10.4 km|
|275 hPa |9.7 km|
|300 hPa |9.2 km|
|350 hPa |8.1 km|
|400 hPa |7.2 km|
|450 hPa |6.3 km|
|500 hPa |5.6 km|
|550 hPa |4.9 km|
|600 hPa |4.2 km|
|650 hPa |3.6 km|
|700 hPa |3 km|
|750 hPa |2.5 km|
|800 hPa |1900 m|
|850 hPa |1500 m|
|875 hPa |1200 m|
|900 hPa |1000 m|
|925 hPa |800 m|
|950 hPa |500 m|
|970 hPa |370 m|
|985 hPa |240 m|
|1000 hPa |110 m|
|1015 hPa |-10 m|