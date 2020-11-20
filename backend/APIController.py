from flask import Flask

import APIService

app = Flask(__name__)

@app.route('/<city>/<region>')
def getWeather(city, region):
    return APIService.getWeather(city, region)
