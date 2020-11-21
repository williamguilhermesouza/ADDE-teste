import { HttpClient, HttpRequest, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Weather } from './weather';

@Injectable({
  providedIn: 'root'
})
export class WeatherService {
  private readonly API = `${environment.API}`;

  constructor(private http: HttpClient) { }

  getWeather(city, region) {
    return this.http.get<Weather[]>(`${this.API}${city}/${region}`);
  }

  getLocationWeather(lat, lon) {
    return this.http.get<Weather>(`${this.API}location-weather/${lat}/${lon}`);
  }

}
