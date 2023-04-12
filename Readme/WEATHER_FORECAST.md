# Select your location, weather variables and start using the API.


## Code Example :

```python

#from openmeteo_py.Daily.Marine import Marine as Daily
from openmeteo_py import OWmanager
from openmeteo_py.Hourly.HourlyForecast import HourlyForecast
from openmeteo_py.Daily.DailyForecast import DailyForecast
from openmeteo_py.Options.ForecastOptions import ForecastOptions
from openmeteo_py.Utils.constants import *

# Latitude, Longitude 
longitude = 33.89
latitude =  -6.31

hourly = HourlyForecast()
daily = DailyForecast()

#here we provide a bit more information as we want to pull also the data of past days
options = ForecastOptions(latitude,longitude,False,celsius,kmh,mm,iso8601,utc,2)

#notice that we had to give the value "None" for the hourly parameter,otherwise you'll be filling the hourly parameter instead of the daily one.
mgr = OWmanager(options,OWmanager.forecast,hourly.shortwave_radiation(),daily.shortwave_radiation_sum())


# Download data
meteo = mgr.get_data(1)

print(meteo)

```


Options :

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
|start_date,end_date   |String (yyyy-mm-dd)	        |No|
|models   |String array|No|  auto|
|past_days	            |Integer (0-2)	|No|          0|
|cell_selection   |String|No|  land|


Hourly Parameter Definition :

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
|diffuse_radiation	     |   Preceding hour mean	|    W/mv²|
|vapor_pressure_deficit	  |  Instant	   |             kPa|
|evapotranspiration	       | Preceding hour sum|	    mm (inch)|
|precipitation	            |Preceding hour sum	|    mm (inch)|
|weathercode	               | Instant	  |              WMO code|
|snow_depth	                |Instant	|                meters|
|freezinglevel_height|	    Instant	     |           meters|
|soil_temperature_0cm |       Instant |                °C (°F)|
|soil_temperature_6cm  |      Instant     |            °C (°F)|
|soil_temperature_18cm  |     Instant  |               °C (°F)|
|soil_temperature_54cm	 |   Instant	     |           °C (°F)|
|soil_moisture_0_1cm      |   Instant   |              m³/m³|
|soil_moisture_1_3cm       |  Instant       |          m³/m³|
|soil_moisture_3_9cm        | Instant    |             m³/m³|
|soil_moisture_9_27cm        |Instant        |         m³/m³|
|cape|	    Instant	      |           	J/kg|
|et0_fao_evapotranspiration|	    Preceding hour sum	      |          mm (inch)|
|rain|	    Preceding hour sum	      |          mm (inch)|
|showers|	    Preceding hour sum	      |          mm (inch)|
|visibility|	    Instant	      |          meters|
|precipitation_probability|	     	Preceding hour probability      |          %|
|is_day|	    Instant	      |          Dimensionless|
|all|-|-|

Daily Parameter Definition

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


WMO Weather interpretation codes (WW)

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


