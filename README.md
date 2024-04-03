[![Documentation Status](https://readthedocs.org/projects/openmeteo-py/badge/?version=latest)](https://openmeteo-py.readthedocs.io/en/latest/?badge=latest)

<h1 align="center"> OpenmeteoPy </h1>

<p align="center">
  <img  src="https://cdn.substack.com/image/fetch/w_1360,c_limit,f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd0d7953-5a9d-441c-b59f-4cde244503a1_934x461.png">
</p>

Download Meteorological Data from OPEN-METEO API (https://open-meteo.com/en)

Open-Meteo collaborates with National Weather Services providing Open Data with 11 to 2 km resolution. Our high performance APIs select the best weather model for your location and provide data as a simple JSON API.


APIs are free without any API key for open-source developers and non-commercial use. You can embed them directly into your app.

##  What is it?
openmeteopy is a client Python wrapper library for Open-Meteo  web API. It allows quick and easy consumption of Open-Meteo data from Python applications via a simple object model and in a human-friendly fashion.

You can use all Openmeteo's available APIs,which are 14 (explained in the table below).

openmeteopy runs on Python 3.6+.

Full documentation is reported here: [DOCUMENTATION](https://openmeteo-py.readthedocs.io/en/latest/index.html).

#### Installation (pypi)
```bash
working on it
```
#### Installation (manually)
```bash
git clone https://github.com/m0rp43us/openmeteopy
cd openmeteopy-main/
pip install .
```
## APIs
|API	            |Description|Documentation        |Options Class	|Hourly Class|Daily Class|15 Minutes Class|
|-----|--------|--------|--------|---------|---------|----------|
|Weather forecast | Select your location, weather variables and start using the API.|[Weather Forecast](/readme/WEATHER_FORECAST.md) | ```ForecastOptions()``` | ```HourlyForecast()```|```DailyForecast()```|-|
|Historical Weather | Discover how weather has shaped our world from 1940 until now|[Historical Weather](/readme/HISTORICAL_WEATHER.md) | ```HistoricalOptions()``` | ```HourlyHistorical()```|```DailyHistorical()```|-|
|ECMWF Weather Forecast | Global High Frequency Forecasts at 0.4° resolution |[ECMWF Weather Forecast](/readme/ECMWF.md)  |```EcmwfOptions()``` | ``` HourlyEcmwf()```|-|-|
|GFS & HRRR Forecast  |Global GFS model combined with hourly HRRR updates at 3-km resolution |[GFS & HRRR Forecast ](/readme/GFS_HRRR_FORECAST.md) | ```GfsOptions()``` | ```HourlyGfs()```|```DailyGfs()```|-|
|MeteoFrance  |Global ARPEGE model combined with high resolution AROME model| [MeteoFrance ](/readme/METEOFRANCE.md) | ```MeteoFranceOptions()``` | ```HourlyMeteoFrance()```|```DailyMeteoFrance()```|-|
|DWD ICON |Open data weather forecasts from the German weather service DWD |[DWD ICON](/readme/DWD_ICON.md) | ```DwdOptions()``` | ```HourlyDwd()```|```DailyDwd()```|```FifteenMinutesDwd()```|
|JMA |5-km high resolution forecasts for Japan, Korea, parts of China and Russia |[JMA](/readme/JMA.md) | ```JmaOptions()``` | ```HourlyJma()```|```DailyJma()```|-|
|MET Norway |Hourly updates & 1 km forecasts for Scandinavia| [MET Norway](/readme/MET_NORWAY.md) | ```MetnoOptions()``` | ```HourlyMetno()```|-|-|
|GEM  | 2.5 km high resolution forecasts for North America|[GEM](/readme/GEM.md) | ```GemOptions()``` | ```HourlyGem()```|```DailyGem()```|-|
|Marine Weather | Hourly wave forecasts at 5 km resolution|[Marine Weather](/readme/MARINE_WEATHER.md) | ```MarineOptions()``` | ```HourlyMarine()```|```DailyMarine()```|-|
|Air Quality | Pollutants and pollen forecast in 11 km resolution|[Air Quality](/readme/AIR_QUALITY.md) | ```AirQualityOptions()``` | ```HourlyAirQuality()```|-|-|
|Geocoding | Search locations in any language globally|[Geocoding](/readme/GEOCODING.md) | ```GeocodingOptions()``` | - |-|-|
|Elevation | 90 meter resolution digital elevation model|[Elevation](/readme/ELEVATION.md) | ```ElevationOptions()``` | -|-|-|
|Global Flood | Simulated river discharge at 5 km resolution from 1984 up to 7 months forecast|[Global Flood](/readme/GLOBAL_FLOOD.md) | ```FloodOptions()``` | - |```DailyForecast()```|-|

# Output formats:

You can get your output in python dictionary, json string, pandas DataFrame, numpy array. Additionally, you can save APIs response to files in csv, excel or json format.

|Output | Library function |
|----|-----|
|dict (full server response) | ```client._fetch()```|
|dict (cleaned version) | ```client.get_dict()```|
|json string (cleaned version) |``client.get_json_str()``|
|numpy array |``client.get_numpy()``|
|pandas DataFrame (keys are dates,value are correspongding values) | ```client.get_pandas()```|
|save to csv (keys are dates,value are correspongding values)| ```save_csv(<filepath>)```|
|save to excel (keys are dates,value are correspongding values) | ```save_excel(<filepath>)```|
|save to json | ```save_json(<filepath>)```|



## Upcoming Changes,updates,things to do :

- Add the other 2 variables to ECWMF pressure level parameters
- remove pressure level variables from JMA (Remove inheritence from FranceMeteo)
- Add Support of Date Types (input and output)
- Add versionning and package to pypi


