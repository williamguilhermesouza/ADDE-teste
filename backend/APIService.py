import requests

  
def getWeather(city, region):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":f'{city},{region}',"units":"metric"}

    headers = {
        'x-rapidapi-key': "71d88ab42fmshe11d43503705b84p13f999jsn02e75f42af27",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text