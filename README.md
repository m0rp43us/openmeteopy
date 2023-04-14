<h1 align="center"> OpenmeteoPy </h1>

<p align="center">
  <img  src="https://cdn.substack.com/image/fetch/w_1360,c_limit,f_auto,q_auto:best,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd0d7953-5a9d-441c-b59f-4cde244503a1_934x461.png">
</p>

Download Meteorological Data from OPEN-METEO API (https://open-meteo.com/en)

Open-Meteo collaborates with National Weather Services providing Open Data with 11 to 2 km resolution. Our high performance APIs select the best weather model for your location and provide data as a simple JSON API.


APIs are free without any API key for open-source developers and non-commercial use. You can embed them directly into your app.

##  What is it?
openmeteopy is a client Python wrapper library for Open-Meteo  web API. It allows quick and easy consumption of OM data from Python applications via a simple object model and in a human-friendly fashion.

You can use all Openmeteo's available APIs,which are 14 (explained in the table below).

openmeteopy runs on Python 3.6+.

print(mgr.get_data())

#### Installation (pypi)
```bash
working on it
```
#### Installation (manually)
```bash
git clone https://github.com/m0rp43us/openmeteopy
cd openmeteopy-main/
pip3 install .
```
## APIs
|API	            |Description|Documentation        |Options Class	|Hourly Class|Daily Class|15 Minutes Class|
|-----|--------|--------|--------|---------|---------|----------|
|Weather forecast | Select your location, weather variables and start using the API.|[weather forecast](/Readme/WEATHER_FORECAST.md) | ```ForecastOptions()``` | ```HourlyForecast()```|```DailyForecast()```|-|
|Historical Weather | Discover how weather has shaped our world from 1940 until now|[historical weather](/Readme/HISTORICAL_WEATHER.md) | ```HistoricalOptions()``` | ```HourlyHistorical()```|```DailyHistorical()```|-|
|ECMWF Weather Forecast | Global High Frequency Forecasts at 0.4° resolution |[ECMWF Weather Forecast](/Readme/ECMWF_Weather_Forecast.md)  |```EcmwfOptions()``` | ``` HourlyEcmwf()```|-|-|
|GFS & HRRR Forecast  |Global GFS model combined with hourly HRRR updates at 3-km resolution |[GFS & HRRR Forecast ](/Readme/GFS_HRRR_FORECAST.md) | ```GfsOptions()``` | ```HourlyGfs()```|```DailyGfs()```|-|
|MeteoFrance  |Global ARPEGE model combined with high resolution AROME model| [MeteoFrance ](/Readme/METEOFRANCE.md) | ```MeteoFranceOptions()``` | ```HourlyMeteoFrance()```|```DailyMeteoFrance()```|-|
|DWD ICON |Open data weather forecasts from the German weather service DWD |[DWD ICON](/Readme/DWD_ICON.md) | ```DwdOptions()``` | ```HourlyDwd()```|```DailyDwd()```|```FifteenMinutesDwd()```|
|JMA |5-km high resolution forecasts for Japan, Korea, parts of China and Russia |[JMA](/Readme/JMA.md) | ```JmaOptions()``` | ```HourlyJma()```|```DailyJma()```|-|
|MET Norway |Hourly updates & 1 km forecasts for Scandinavia| [MET Norway](/Readme/MET_Norway.md) | ```MetnoOptions()``` | ```HourlyMetno()```|-|-|
|GEM  | 2.5 km high resolution forecasts for North America|[GEM](/Readme/WEATHER_FORECAST.md) | ```GemOptions()``` | ```HourlyGem()```|```DailyGem()```|-|
|Marine Weather | Hourly wave forecasts at 5 km resolution|[Marine Weather](/Readme/MARINE_WEATHER.md) | ```MarineOptions()``` | ```HourlyMarine()```|```DailyMarine()```|-|
|Air Quality | Pollutants and pollen forecast in 11 km resolution|[Air Quality](/Readme/AIR_QUALITY.md) | ```AirQualityOptions()``` | ```HourlyAirQuality()```|-|-|
|Geocoding | Search locations in any language globally|[Geocoding](/Readme/GEOCODING.md) | ```GeocodingOptions()``` | - |-|-|
|Elevation | 90 meter resolution digital elevation model|[Elevation](/Readme/ELEVATION.md) | ```ElevationOptions()``` | -|-|-|
|Global Flood | Simulated river discharge at 5 km resolution from 1984 up to 7 months forecast|[Global Flood](/Readme/GLOBAL_FLOOD.md) | ```FloodOptions()``` | - |```DailyForecast()```|-|

# Output formats : (I know it kindda sucks with integers as inputs,will change it soon)

You can get your output in json,dataframe or save it as csv or excel file as follows : get_data(output = 0,file = 0,filepath = None):
|Ooutput|```get_data``` Method values|
|----|-----|
|json (server response) | ```get_data()```|
|json (keys are dates,value are correspongding values) | ```get_data(1)```|
|json (keys are dates,value are correspongding values) saved into a json file | ```get_data(1,1)```|
|csv (keys are dates,value are correspongding values) saved into a csv file | ```get_data(1,1,'path')```|
|excel (keys are dates,value are correspongding values) saved into a excel file | ```get_data(1,2,'path')```|
|dataframe in excel (keys are dates,value are correspongding values) saved into a excel file | ```get_data(1,3,'path')```|


## Upcoming Changes,updates,things to do :

- Add the other 2 variables to ECWMF pressure level parameters
- Change ```get_data()``` method to a more developper friendly method
- Add Documentation for ```dataframit()``` and ```jsonify()```
- remove pressure level variables from JMA (Remove inheritence from FranceMeteo)
- Add Support of Date Types (input and output)
- Add versionning and package to pypi
- Clean and add corresponding comments
- Maybe Refactor OWmanager Class and add inheritence for a more Dev friendly Methods
- Readthedocs


### Contributions (coding, testing, packaging, reporting issues) are more than welcome ! 
