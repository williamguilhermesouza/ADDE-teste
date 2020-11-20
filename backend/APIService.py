import requests

def locationWeather(lat, lon):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    ## building the query to the api
    querystring = {"lat":lat,"lon":lon,"units":"metric"}

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
    weather = json_response['weather'][0]['main']
    icon_code = json_response['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/w/{icon_code}.png'

    ## creating desired object with data
    response = { 
        'city': city, 
        'weather': weather,
        'temperature': temperature,
        'icon_code':icon_code,
        'icon_url': icon_url
         }

    ## returning desired response
    print(response)
    return response
    
  
## main get weather request
def getWeather(city, region):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    ## building the query to the api
    querystring = {"q":f'{city},{region}',"units":"metric"}

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
    weather = json_response['weather'][0]['main']
    icon_code = json_response['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/w/{icon_code}.png'

    ## creating desired object with data
    response = { 
        'city': city, 
        'weather': weather,
        'temperature': temperature,
        'icon_code':icon_code,
        'icon_url': icon_url
         }

    ## returning desired response
    print(response)
    return response