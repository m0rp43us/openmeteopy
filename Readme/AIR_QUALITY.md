# Search locations in any language globally


## Parameters


### Options :

|Parameter	            |Format	        |Required	|Default| 
|-----|--------|--------|--------|
|latitude, longitude	    | 	Floating point	|Yes|   - |
|domains	            |String array 		|No|          auto
|timeformat	        | 	String	        |No|          iso8601|
|timezone    |String	        |No|           	GMT|
|past_days    |Integer (0-2)	        |No|           	0|
|start_end  |Boolean|No|False|
|start_date,end_date   |String (yyyy-mm-dd)	        |No|           	-|
|cell_selection   |String	        |No|           	nearest|

### Hourly Parameter Definition :

|Variable                |Valid time|	            Unit|
|-----|----|-----|
|pm10|	            Instant	 |               μg/m³|
|pm2_5|	            Instant	 |               μg/m³|
|carbon_monoxide|	            Instant	 |               μg/m³|
|nitrogen_dioxide|	            Instant	 |               μg/m³|
|sulphur_dioxide|	        Instant	  |              μg/m³|
|ozone|         Instant	 |               μg/m³|
|ammonia|    Instant	      |          μg/m³|
|aerosol_optical_depth|   Instant	       |         Dimensionless 	|
|dust|    Instant	      |          μg/m³|
|uv_index|   Instant	        |       Index|
|uv_index_clear_sky|  Instant	       |        Index|
|alder_pollen| Instant           |      Grains/m³|
|birch_pollen|               Instant            |     Grains/m³|
|grass_pollen|              Instant             |  Grains/m³|
|mugwort_pollen|            Instant	             |   Grains/m³|
|olive_pollen|           Instant|                 Grains/m³|
|ragweed_pollen|          Instant |                Grains/m³|
|european_aqi|         Instant  |               European AQI|
|european_aqi_pm2_5|       Instant	  |              European AQI|
|european_aqi_pm10|      Instant|	    European AQI|
|european_aqi_no2 |       Instant	    |European AQI|
|european_aqi_o3|  Instant	|    European AQI|
|european_aqi_so2|   Instant	|   European AQI|
|us_aqi|  Instant	   |             U.S. AQI|
|us_aqi_pm2_5| Instant|	    U.S. AQI|
|us_aqi_pm10|Instant	|    U.S. AQI|
|us_aqi_no2| Instant	  |              U.S. AQI|
|us_aqi_o3|Instant	|                U.S. AQI|
|us_aqi_so2|	    Instant	     |           U.S. AQI|
|us_aqi_co|       Instant |                U.S. AQI|

