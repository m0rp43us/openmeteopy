# Open data weather forecasts from the German weather service DWD

# Code Example :

```python

from openmeteo_py import OWmanager
from openmeteo_py.Hourly.HourlyDwd import HourlyDwd
from openmeteo_py.Daily.DailyDwd import DailyDwd
from openmeteo_py.Options.DwdOptions import DwdOptions
from openmeteo_py.FifteenMinutes.FifteenMinutesDwd import FiftennMinutesDwd


# Latitude, Longitude 
longitude = 139.817413
latitude =  35.672855	

hourly = HourlyDwd()
daily = DailyDwd()
minutes_15 = FiftennMinutesDwd()
options = DwdOptions(latitude,longitude)

mgr = OWmanager(options,OWmanager.dwd_icon,hourly.all(),daily.all(),minutes_15.all())


# Download data
meteo = mgr.get_data()

print(meteo)

```

## Parameters

|Parameter	            |Format	        |Required	|Default|
|-----|--------|--------|--------|
|latitude, longitude	    |Floating point	|Yes|        |
|current_weather	        |Bool	        |No|          false|
|temperature_unit	    |String	        |No|          celsius|
|windspeed_unit	        |String	        |No|          kmh|
|precipitation_unit	    |String          |No|         kmh|
|timeformat	            |String	        |No|          iso8601|
|timezone	            |String	        |No|	        UTC|.
|start_end  |Boolean|No|False|
|start_date,end_date   |String (yyyy-mm-dd)	        |No|
|past_days	            |Integer (0-2)	|No|          0|
|cell_selection   |String|No|  land|

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
|direct_normal_irradiance	      |  Preceding hour mean	|    W/m²|
|diffuse_radiation	     |   Preceding hour mean	|    W/mv²|
|vapor_pressure_deficit	  |  Instant	   |             kPa|
|evapotranspiration	       | Preceding hour sum|	    mm (inch)|
|precipitation	            |Preceding hour sum	|    mm (inch)|
|weathercode	               | Instant	  |              WMO code|
|snow_depth	                |Instant	|                meters|
|snow_height	                |Instant	|                meters|
|freezinglevel_height|	    Instant	     |           meters|
|soil_temperature_0cm |       Instant |                °C (°F)|
|soil_temperature_6cm  |      Instant     |            °C (°F)|
|soil_temperature_18cm  |     Instant  |               °C (°F)|
|soil_temperature_54cm	 |   Instant	     |           °C (°F)|
|soil_moisture_0_1cm      |   Instant   |              m³/m³|
|soil_moisture_1_3cm       |  Instant       |          m³/m³|
|soil_moisture_3_9cm        | Instant    |             m³/m³|
|soil_moisture_9_27cm        |Instant        |         m³/m³|
|soil_moisture_27_81cm        |Instant        |         m³/m³|
|cape|	    Instant	      |           	J/kg|
|et0_fao_evapotranspiration|	    Preceding hour sum	      |          mm (inch)|
|rain|	    Preceding hour sum	      |          mm (inch)|
|showers|	    Preceding hour sum	      |          mm (inch)|
|updraft|	    Instant	      |          m/s|
|lightning_potential|	    Instant	      |          J/kg|
|all|-|-|

## 15-Minutely Parameter Definition

|Variable	        |            Unit|
|----|------|
|shortwave_radiation            |  W/m²|
|direct_radiation	          |  W/m²|
|direct_normal_irradiance    |   W/m²|
|diffuse_radiation	  |  W/m²|
|lightning_potential	       |     J/kg|
|precipitation	          |  mm |
|snowfall	                 |   cm|
|snowfall_height                      |   meters|
|freezinglevel_height                      |   meters|
|cape	                     |   J/kg|
|rain|mm |
|all|-|


### Pressure Level Variables

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

### Pressure level methods

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

### Daily Parameter Definition

|Variable	        |            Unit|
|----|------|
|weathercode| WMO Code|
|temperature_2m_max            |  °C (°F)|
|temperature_2m_min	          |  °C (°F)|
|apparent_temperature_max    |    °C (°F)|
|apparent_temperature_min	  |  °C (°F)|
|rain_sum|mm|
|precipitation_sum	       |     mm|
|precipitation_hours	          |  hours|
|snowfall_sum|cm|
|showers_sum|mm|
|sunrise                      |   iso8601|
|sunset	                     |   iso8601|
|windspeed_10m_max|km/h (mph, m/s, knots)|
|windgusts_10m_max|km/h (mph, m/s, knots)|
|winddirection_10m_dominant|	    °|
|shortwave_radiation_sum|	        MJ/m²|
|et0_fao_evapotranspiration|	        mm|
|all|-|

### WMO Weather interpretation codes (WW)

|code     |   Description|
|------|-------|
|0|	            Clear sky|
|1, 2, 3|	        Mainly clear, partly cloudy, and overcast|
|45, 48	 |       Fog and depositing rime fog|
|51, 53, 55|	    Drizzle: Light, moderate, and dense intensity|
|56, 57	    |    Freezing Drizzle: Light and dense intensity|
|61, 63, 65	 |   Rain: Slight, moderate and heavy intensity|
|66, 67	    |    Freezing Rain: Light and heavy intensity|
|71, 73, 75	 |   Snow fall: Slight, moderate, and heavy intensity|
|77	          |  Snow grains|
|80, 81, 82|	    Rain showers: Slight, moderate, and violent|
|85, 86	    |    Snow showers slight and heavy|
|95 *	       | Thunderstorm: Slight or moderate|
|96, 99 *	    |Thunderstorm with slight and heavy hail|

