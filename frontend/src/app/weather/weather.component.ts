import { Component, OnInit } from '@angular/core';
import { Weather } from './weather';
import { WeatherService } from './weather.service';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css'],
})
export class WeatherComponent implements OnInit {
  weather: Weather;

  constructor(private weatherService: WeatherService) { }

  ngOnInit(): void {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition( position => {
        const longitude = position.coords.longitude;
        const latitude = position.coords.latitude;
        console.log(longitude, latitude);
      })
    } else {
      console.log("No default location");
    }

    this.weatherService.getWeather('niteroi', 'br')
    .subscribe(data => this.weather = data);
  }

  getWeather(city: string, region: string) {
    this.weatherService.getWeather(city, region)
    .subscribe(data => this.weather =data);    
  }

}
