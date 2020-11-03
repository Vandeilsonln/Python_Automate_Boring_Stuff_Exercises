#! python3
# quickWeather.py - Prints the weather for a location frmo the command line.


import json, requests, sys, pprint


# Compute location from command line arguments.
#if len(sys.argv) < 2:
 #   print('Usage: quickWeather.py location')
  #  sys.exit()
location = 'Sao Paulo, Brazil' #' '.join(sys.argv[1:])
key = ''
# Download the JSON data from OpenWeatherMap.org's API.
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&lang=pt_br&appid={key}'

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

pprint.pprint(weatherData)