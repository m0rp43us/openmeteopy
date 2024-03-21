#

## Code Example :

```python
from openmeteopy import OpenMeteo
from openmeteopy.hourly import HourlyHistorical
from openmeteopy.daily import DailyHistorical
from openmeteopy.options import HistoricalOptions
from openmeteopy.utils.constants import *

# Latitude, Longitude 
longitude = 33.89
latitude =  -6.31

hourly = HourlyHistorical()
daily = DailyHistorical()
options = HistoricalOptions(latitude,
                            longitude, 
                            start_date="2022-12-31",
                            end_date="2023-02-26")

mgr = OpenMeteo(options, hourly.all(), daily.all())

# Download data
meteo = mgr.get_pandas()
print(meteo)
```

## Options :

|Parameter	            |Format	        |Required	|Default|
|-----|--------|--------|--------|
|latitude, longitude	    |Floating point	|Yes|        |
|current_weather	        |Bool	        |No|          false|
|temperature_unit	    |String	        |No|          celsius|
|windspeed_unit	        |String	        |No|          kmh|
|precipitation_unit	    |String          |No|         kmh|
|timeformat	            |String	        |No|          iso8601|
|timezone	            |String	        |No|	        UTC|
|start_end  |Boolean|No|False|
|start_date,end_date   |String (yyyy-mm-dd)	        |Yes|           	-|
|cell_selection   |String	        |No|           	nearest|

## Hourly Parameter Definition :

|Variable                |Valid time|	            Unit|
|-----|----|-----|
|temperature_2m|	            Instant	 |               °C (°F)|
|relativehumidity_2m|	        Instant	  |              %|
|dewpoint_2m	       |         Instant	 |               °C (°F)|
|apparent_temperature	|    Instant	      |          °C (°F)|
|pressure_msl,surface_pressure	         |   Instant	       |         hPa|
|cloudcover	            |    Instant	      |          %|
|cloudcover_low	         |   Instant	        |        %|
|cloudcover_mid	          |  Instant	       |        %|
|cloudcover_high	         |   Instant	       |         %|
|windspeed_10m              | Instant           |      km/h (mph, m/s, knots)|
|winddirection_10m|           Instant|                 °|
|windgusts_10m	      |      Preceding hour max|	    km/h (mph, m/s)|
|shortwave_radiation	 |       Preceding hour mean	    W/m²|
|direct_radiation	      |  Preceding hour mean	|    W/m²|
|diffuse_radiation	     |   Preceding hour mean	|    W/mv²|
|vapor_pressure_deficit	  |  Instant	   |             kPa|
|precipitation	            |Preceding hour sum	|    mm (inch)|
|weathercode	               | Instant	  |              WMO code|
|cape|	    Instant	      |           	J/kg|
|et0_fao_evapotranspiration|	    Preceding hour sum	      |          mm (inch)|
|snowfall|	    Preceding hour sum	      |          cm (inch)|
|soil_temperature_0_to_7cm|	    Instant  |          °C (°F)|
|soil_temperature_7_to_28cm|	Instant      |          °C (°F)
|soil_temperature_28_to_100cm|	Instant      |          °C (°F)
|soil_temperature_100_to_255cm|	Instant      |          °C (°F)
|soil_moisture_0_to_7cm|	    Instant    |          m³/m³|
|soil_moisture_7_to_28cm|	    Instant    |          m³/m³|
|soil_moisture_28_to_100cm|	    Instant    |          m³/m³|
|soil_moisture_100_to_255cm|	Instant	      |       m³/m³|
|all|-|-|

### Daily Parameter Definition

|Variable	        |            Unit|
|----|------|
|temperature_2m_max            |  °C (°F)|
|temperature_2m_min	          |  °C (°F)|
|apparent_temperature_max    |    °C (°F)|
|apparent_temperature_min	  |  °C (°F)|
|precipitation_sum	       |     mm|
|precipitation_hours	          |  hours|
|snowfall_sum|cm|
|sunrise                      |   iso8601|
|sunset	                     |   iso8601|
|windspeed_10m_max|km/h (mph, m/s, knots)|
|windgusts_10m_max	        |    km/h (mph, m/s, knots)|
|winddirection_10m_dominant|	    °|
|shortwave_radiation_sum|	        MJ/m²|
|et0_fao_evapotranspiration|	        mm|
|all|-|

