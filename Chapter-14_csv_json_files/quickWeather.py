#! python3
# quickWeather.py - Prints the weather for a location frmo the command line.


import json, requests, sys


# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

#TODO: Download the JSON data from OpenWeatherMap.org's API.
url = f'http:api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3'

response = requests.get(url)
response.raise_for_status()

#TODO: Load JSON data into a Python variable.