APPID = 'yourAPIKey'

import json, requests, sys

if len(sys.argv) < 2:
    print('Usage: openWeather.py city_name')
    sys.exit()

location = ' '.join(sys.argv[1:])
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={APPID}'
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
print(f"Current weather in {location} is:")
desc = weatherData['weather'][0]['description']
main = weatherData['weather'][0]['main']
print(main + ' - ' + desc)
