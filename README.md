<h1 align="center"> OpenmeteoPy </h1>

<p align="center">
  <img  src="https://cdn.substack.com/image/fetch/w_1360,c_limit,f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd0d7953-5a9d-441c-b59f-4cde244503a1_934x461.png">
</p>

Download Meteorological Data from OPEN-METEO API (https://open-meteo.com/en)

Open-Meteo collaborates with National Weather Services providing Open Data with 11 to 2 km resolution. Our high performance APIs select the best weather model for your location and provide data as a simple JSON API.


APIs are free without any API key for open-source developers and non-commercial use. You can embed them directly into your app.

##  What is it?
openmeteopy is a client Python wrapper library for Open-Meteo  web API. It allows quick and easy consumption of OM data from Python applications via a simple object model and in a human-friendly fashion.

openmeteopy runs on Python 3.6+.

print(mgr.get_data())

#### Installation (pypi)
```bash
pip install openmeteo-py==0.0.1
```
#### Installation (manually)
```bash
git clone https://github.com/m0rp43us/openmeteopy
cd openmeteopy-main/
pip3 install .
```
###Parameters


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
|past_days	            |Integer (0-2)	|No|          0|

Hourly Parameter Definition :

|Variable                |Valid time|	            Unit|
|-----|----|-----|
|temperature_2m|	            Instant	 |               °C (°F)|
|relativehumidity_2m|	        Instant	  |              %|
|dewpoint_2m	       |         Instant	 |               °C (°F)|
|apparent_temperature	|    Instant	      |          °C (°F)|
|pressure_msl	         |   Instant	       |         hPa|
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
|soil_moisture_27_81cm|	    Instant	      |          m³/m³|
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

### Example

Download Meteorological data

```python
from openmeteo_py import Hourly,Daily,Options,OWmanager

# Latitude, Longitude for Rabat,Morocco
latitude = 33.9842
longitude = -6.8675

hourly = Hourly()
daily = Daily()
options = Options(latitude,longitude)

mgr = OWmanager(options,
    hourly.all(),
    daily.all())


# Download data
meteo = mgr.get_data()

print(meteo)

```



### :heart:  Contributors (coding, testing, packaging, reporting issues) are welcome! :heart:
