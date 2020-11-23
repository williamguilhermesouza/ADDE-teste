from unittest.mock import Mock, patch
from nose.tools import assert_equal
from backend import APIService

## testing locationWeather route
@patch('backend.APIService.requests.request')
def test_locationWeather(mock_get):

    ## mock return value from API 
    mockValue = ({"coord":{"lon":-0.13,"lat":51.51},
        "weather":[{"id":741,"main":"Fog","description":"fog","icon":"50n"}],
        "base":"stations","main":{"temp":284.04,"pressure":1011,"humidity":93,
        "tempmin":280.93,"tempmax":287.04},"visibility":10000,"wind":{"speed":1.5},
        "clouds":{"all":20},"dt":1570234102,"sys":{"type":1,"id":1417,"message":0.0102,
        "country":"GB","sunrise":1570255614,"sunset":1570296659},
        "timezone":3600,"id":2643743,"name":"London","cod":200})

    ## expected response from the function
    expected_response = {
        'city': 'London', 
        'weekday': 'Hoje', 
        'weather': 'fog', 
        'temperature': 284, 
        'icon_code': '50n', 
        'icon_url': 'http://openweathermap.org/img/w/50n.png'
        }

    ## making the external API mock the mock value
    mock_get.return_value.json.return_value = mockValue

    ## getting the response and testing if it is as expected
    response = APIService.locationWeather(40, -90)
    assert_equal(response, expected_response)

## testing getWeather route
@patch('backend.APIService.requests.request')
def test_getWeather(mock_get):


    ## mock return value from API 
    mockValue = {'city': {'id': 3456283, 'name': 'Niterói', 
        'coord': {'lon': -43.1036, 'lat': -22.8833}, 'country': 'BR', 
        'population': 456456, 'timezone': -10800}, 'cod': '200', 
        'message': 3.3862967, 'cnt': 7, 
        'list': [{'dt': 1606140000, 'sunrise': 1606118340, 'sunset': 1606166357, 
        'temp': {'day': 26.23, 'min': 21.52, 'max': 26.23, 'night': 22.53, 'eve': 23.89, 'morn': 21.61}, 
        'feels_like': {'day': 27.24, 'night': 22.96, 'eve': 23.91, 'morn': 22.93}, 
        'pressure': 1019, 'humidity': 74, 
        'weather': [{'id': 501, 'main': 'Rain', 'description': 'chuva moderada', 'icon': '10d'}], 
        'speed': 4.69, 'deg': 119, 'clouds': 75, 'pop': 0.88, 'rain': 3.71}, 
        {'dt': 1606226400, 'sunrise': 1606204734, 'sunset': 1606252799, 
        'temp': {'day': 26.49, 'min': 21.4, 'max': 26.49, 'night': 22.84, 
        'eve': 24.25, 'morn': 21.63}, 'feels_like': {'day': 26.81, 'night': 23.2, 'eve': 24.17, 'morn': 23.26}, 
        'pressure': 1021, 'humidity': 65, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'chuva fraca', 'icon': '10d'}], 
        'speed': 4.4, 'deg': 121, 'clouds': 34, 'pop': 0.58, 'rain': 1.53}, {'dt': 1606312800, 'sunrise': 1606291129, 
        'sunset': 1606339240, 'temp': {'day': 28.8, 'min': 21.41, 'max': 28.8, 'night': 23.46, 'eve': 25.28, 'morn': 21.45}, 
        'feels_like': {'day': 29.39, 'night': 24.86, 'eve': 25.34, 'morn': 23.25}, 'pressure': 1019, 'humidity': 56, 
        'weather': [{'id': 500, 'main': 'Rain', 'description': 'chuva fraca', 'icon': '10d'}], 
        'speed': 3.86, 'deg': 111, 'clouds': 2, 'pop': 0.36, 'rain': 0.24}, {'dt': 1606399200, 'sunrise': 1606377526, 
        'sunset': 1606425682, 'temp': {'day': 30.53, 'min': 22.08, 'max': 30.88, 'night': 25.43, 'eve': 28, 'morn': 22.28}, 
        'feels_like': {'day': 31.87, 'night': 27.17, 'eve': 28.96, 'morn': 23.9}, 'pressure': 1015, 
        'humidity': 48, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'céu limpo', 'icon': '01d'}], 
        'speed': 2.23, 'deg': 119, 'clouds': 0, 'pop': 0.19}, {'dt': 1606485600, 'sunrise': 1606463924, 
        'sunset': 1606512124, 'temp': {'day': 31.2, 'min': 22.96, 'max': 31.2, 'night': 25.26, 'eve': 27.71, 'morn': 22.96}, 
        'feels_like': {'day': 32.27, 'night': 27.1, 'eve': 28.38, 'morn': 24.24}, 'pressure': 1015, 'humidity': 45, 
        'weather': [{'id': 800, 'main': 'Clear', 'description': 'céu limpo', 'icon': '01d'}], 'speed': 2.37, 
        'deg': 112, 'clouds': 0, 'pop': 0.02}, {'dt': 1606572000, 'sunrise': 1606550323, 'sunset': 1606598566, 
        'temp': {'day': 31.1, 'min': 23.15, 'max': 31.1, 'night': 24.99, 'eve': 27.72, 'morn': 23.19}, 
        'feels_like': {'day': 32.51, 'night': 25.19, 'eve': 27.71, 'morn': 24.51}, 'pressure': 1015, 'humidity': 49, 
        'weather': [{'id': 800, 'main': 'Clear', 'description': 'céu limpo', 'icon': '01d'}], 'speed': 2.67, 'deg': 97, 
        'clouds': 0, 'pop': 0}, {'dt': 1606658400, 'sunrise': 1606636724, 'sunset': 1606685007, 
        'temp': {'day': 31.82, 'min': 23.15, 'max': 31.82, 'night': 25.63, 'eve': 28.44, 'morn': 23.3}, 
        'feels_like': {'day': 33.26, 'night': 26.78, 'eve': 28.8, 'morn': 24.48}, 'pressure': 1015, 
        'humidity': 46, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'céu limpo', 'icon': '01d'}], 
        'speed': 2.4, 'deg': 78, 'clouds': 10, 'pop': 0}]}


    ## The response is received as a string so 
    # the expected result should have this word
    # in part of it 
    expected_response = "weekday"
    ## making the external API mock the mock value
    mock_get.return_value.json.return_value = mockValue

    ## getting the response and testing if it is as expected
    response = APIService.getWeather('niteroi', 'br')
    assert_equal(response[27:34], expected_response)