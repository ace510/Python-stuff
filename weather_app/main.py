from API_KEY import api_key
import requests

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
# api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={your api key}
# api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={your api key}

weather_preamble = 'http://api.openweathermap.org/data/2.5/weather?q='
weather_location = 'Hillsboro,OR,US&appid='
fancy_opts = '&units=imperial'

request_url = ''.join((weather_preamble,weather_location,api_key,fancy_opts))

# print(request_url)

requestey = requests.get(request_url)

payload = requestey.json()

for i in payload:
    print(f'{i}:{payload[i]}')
    