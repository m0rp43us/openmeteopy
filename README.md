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


#### Installation

```bash
git clone https://github.com/m0rp43us/openmeteopy
cd openmeteopy/
pip3 install .
```
### Example

Download Meteorological data

```python
from openmeteopy import OWmanager,Daily,Hourly,Options

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

```



_Contributors (coding, testing, packaging, reporting issues) are welcome!
