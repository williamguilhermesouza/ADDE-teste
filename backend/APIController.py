from flask import Flask
from flask_caching import Cache

import APIService

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

## /city/region main route, with cache decorators
@app.route('/<city>/<region>')
@cache.memoize(900000)
def getWeather(city, region):
    return APIService.getWeather(city, region)
