#! python3
# quickWeather.py - Prints the weather for a location frmo the command line.


import json, requests, sys, pprint


location = 'Sao Paulo, Brazil'
key = ''
# Download the JSON data from OpenWeatherMap.org's API.
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&lang=pt_br&appid={key}'

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# pprint.pprint(weatherData)

# Print the location's current weather
print(f'Current weather of {location}')
print('Feels like: ', weatherData['main']['feels_like'])
print('Sky: ', weatherData['weather'][0]['description'])
