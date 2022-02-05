# openmeteopy
![openmeteopy](https://cdn.substack.com/image/fetch/w_170,c_limit,f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5ec8df4d-cc18-465d-a9ef-da912c131061_302x302.png)

Download Meteorological Data from OPEN-METEO API (https://open-meteo.com/en)

Open-Meteo collaborates with National Weather Services providing Open Data with 11 to 2 km resolution. Our high performance APIs select the best weather model for your location and provide data as a simple JSON API.


APIs are free without any API key for open-source developers and non-commercial use. You can embed them directly into your app.

##  What is it?
openmeteopy is a client Python wrapper library for Open-Meteo  web API. It allows quick and easy consumption of OM data from Python applications via a simple object model and in a human-friendly fashion.

openmeteopy runs on Python 3.6+.

print(mgr.get_data())

#### Options input parameters

1. latitude - Latitude (float)
2. longitude - Longitude (float)
3. windspeed_unit - wind speed unit (string, optional)
4. precipitation_unit - precipitation amount units (string, optional)
5. timeformat - If format unixtime is selected, all time values are returned in UNIX epoch time in seconds. 
                Please note that all time is then in UTC! For daily values with unix timestamp, please apply utc_offset_seconds again to get the correct date. (string, optional)
6. timezone - If timezone is set, all timestamps are returned as local-time and data is returned starting at 0:00 local-time. 
                Any time zone name from the time zone database is available under timezones.py . (string, optional)
7. past_days - If past_days is set, yesterdays or the day before yesterdays data are also returned.


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


forecast :

|Parameter	            |Format	        |Required	|Default|
|-----|--------|--------|--------|
|latitude, longitude	    |Floating point	|Yes|        |
|hourly	                |String array	|No|
|daily	                |String array	|No|
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



_Contributors (coding, testing, packaging, reporting issues) are welcome!
