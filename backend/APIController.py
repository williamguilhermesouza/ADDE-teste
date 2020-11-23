from flask import Flask
from flask_caching import Cache
from flask_cors import cross_origin

from backend import APIService

## configuring cache
config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 900000
}

## initializing flask with default __name__
app = Flask(__name__)
app.config.from_mapping(config)

## initializing cache
cache = Cache(app)

## get weather based on lat and lon location
@app.route('/location-weather/<lat>/<lon>')
@cache.memoize(900000)
@cross_origin()
def locationWeather(lat, lon):
    return APIService.locationWeather(lat, lon)

## /city/region main route, with cache decorators
@app.route('/<city>/<region>')
@cache.memoize(900000)
@cross_origin()
def getWeather(city, region):
    return APIService.getWeather(city, region)
