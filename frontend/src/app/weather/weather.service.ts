import { HttpClient, HttpRequest, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Weather } from './weather';

@Injectable({
  providedIn: 'root'
})
export class WeatherService {
  private readonly API = 'http://localhost:5000';

  constructor(private http: HttpClient) { }

  getWeather(city, region) {
    return this.http.get<Weather>(`${this.API}/${city}/${region}`);
  }

}
