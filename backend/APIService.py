import requests
import json
from datetime import date


def locationWeather(lat, lon):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    ## building the query to the api
    querystring = {"lat":lat,"lon":lon,"units":"metric", "lang": "pt"}

    ## headers of the query with the key and host
    headers = {
        'x-rapidapi-key': "71d88ab42fmshe11d43503705b84p13f999jsn02e75f42af27",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    ## request response object to be treated
    api_response = requests.request("GET", url, headers=headers, params=querystring)

    ## parsing response to json and extracting desired data
    json_response = api_response.json()

    temperature = json_response['main']['temp']
    city = json_response['name']
    weather = json_response['weather'][0]['description']
    icon_code = json_response['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/w/{icon_code}.png'


    ## creating desired object with data
    response = { 
        'city': city,
        'weekday': 'Hoje',
        'weather': weather,
        'temperature': int(temperature),
        'icon_code':icon_code,
        'icon_url': icon_url
         }

    ## returning desired response
    print(response)
    return response
    
  
## main get weather request
def getWeather(city, region):
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

    ## building the query to the api
    querystring = {"q":f'{city},{region}',"units":"metric","lang":"pt", "cnt": 7}

    ## headers of the query with the key and host
    headers = {
        'x-rapidapi-key': "71d88ab42fmshe11d43503705b84p13f999jsn02e75f42af27",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    ## request response object to be treated
    api_response = requests.request("GET", url, headers=headers, params=querystring)

    ## list of week days to parse into de card data
    week_days = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

    ## parsing response to json and extracting desired data
    json_response = api_response.json()
    city = json_response['city']['name']
    forecasts = json_response['list']

    f = map(lambda data: (
        data := {
            'city': city,
            'weekday': week_days[date.isoweekday(date.fromtimestamp(data['dt'])) - 1],
            'weather': data['weather'][0]['description'],
            'temperature': int(data['temp']['day']),
            'icon_code': data['weather'][0]['icon'],
            'icon_url': 'http://openweathermap.org/img/w/' + data['weather'][0]['icon'] + '.png'
        }
    ), forecasts)

    ## transform map object to list
    f = list(f)

    ## changing week days to today and tomorrow
    f[0]['weekday'] = 'Hoje'
    f[1]['weekday'] = 'Amanhã'


    ## creating desired object with data
    response = json.dumps(f)

    ## returning desired response
    print(response)
    return response