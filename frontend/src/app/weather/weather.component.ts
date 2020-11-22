import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Weather } from './weather';
import { WeatherService } from './weather.service';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css'],
})
export class WeatherComponent implements OnInit {
  weather: Weather[];
  weather$: Observable<Weather>;
  weatherList$: Observable<Weather[]>;

  constructor(private weatherService: WeatherService) { }

  ngOnInit(): void {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition( position => {
        const longitude = position.coords.longitude;
        const latitude = position.coords.latitude;
        console.log(longitude, latitude);
        //this.weatherService.getLocationWeather(latitude, longitude)
        //  .subscribe(data => this.weather = data);
        this.weather$ = this.weatherService.getLocationWeather(latitude, longitude);
      })
    } else {
      console.log("No default location");
    }

    if (window.innerWidth < 800) {
      let wDiv = document.getElementById("weather-div");
      
      wDiv.classList.remove("weather-initial");
      wDiv.classList.remove("weather");
      wDiv.classList.add("weather-vertical");
    }

    
  }

  getWeather(city: string, region: string) {
    this.weatherList$ = this.weatherService.getWeather(city, region);
    console.log(this.weatherList$);

    // removing initial card
    let loc = document.getElementById("location");
    loc.style.display = "none";

    // changing style
    let wDiv = document.getElementById("weather-div");
    wDiv.classList.remove("weather-initial");
    wDiv.classList.add("weather");
  }

  onResize(event): void {
    let width = event.target.innerWidth;
    let wDiv = document.getElementById("weather-div");
    if (width < 800) {
      wDiv.classList.remove("weather-initial");
      wDiv.classList.remove("weather");
      wDiv.classList.add("weather-vertical");
    } else {
      wDiv.classList.remove("weather-vertical");
      wDiv.classList.add("weather");
    }
  }

}
