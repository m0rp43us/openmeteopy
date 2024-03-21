# Search locations in any language globally


## Code Example

```python 
from openmeteopy import OpenMeteo
from openmeteopy.options import GeocodingOptions

options = GeocodingOptions("casablanca")

mgr = OpenMeteo(options)

# Download data
meteo = mgr.get_data()

print(meteo)
```

## Parameters


### Options :

|Parameter	            |Format	        |Required	|Default| 
|-----|--------|--------|--------|
|name	    | 	String	|Yes|   - |
|count	            |Integer	|No|          10|
|format	        | 	String	        |No|          json|
|language    |String	        |No|           	en|

### Result variables :

|Variable                |Format|	             	Description|
|-----|----|-----|
|id|	            Integer	 |               Unique ID for this location|
|name|	            String	 |               Location name. Localized following the ``` language ``` parameter, if possible|
|latitude|	            Floating point	 |               Geographical WGS84 coordinates of this location|
|longitude|	            Floating point	 |               Geographical WGS84 coordinates of this location|
|elevation|	        Floating point	  |    Elevation above mean sea level of this location  	|
|timezone|          	String	 |               Time zone using time zone database definitions, you can find the timezones in ```timezones.py``` |
|feature_code	|     	String	      |           	Type of this location. Following the GeoNames feature_code definition|
|country_code|    	String	       |         2-Character FIPS country code. E.g. DE for Germany|
|country|     	String	      |          Country name,Localized following the ``` language ``` parameter, if possible|
|country_id|   Integer	        |        Unique ID for this country|
|population|  Integer	       |        Number of inhabitants|
|postcodes|   String array 		       |         List of postcodes for this location|
|admin1, admin2, admin3, admin4|String|Name of hierarchical administrative areas this location resides in. Admin1 is the first administrative level. Admin2 the second administrative level,Localized following the ``` language ``` parameter, if possible|
|admin1_id, admin2_id, admin3_id, admin4_id|               Integer           |      	Unique IDs for the administrative areas|