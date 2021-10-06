import requests


class OWmanager():

    url = "https://api.open-meteo.com/v1/forecast?"

    payload = {
            "latitude": 52.52,
            "longitude": 13.41,
            "hourly": "temperature_2m",
            "daily": 'weathercode',
            "timezone": "America/Denver",
            }
    

    def get_data(url,payload):
        print(requests.get(url, params = payload).content)
    pass

OWmanager.get_data(OWmanager.url,OWmanager.payload)

