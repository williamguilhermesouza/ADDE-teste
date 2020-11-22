import { Component, OnInit } from '@angular/core';
import { tsParticles } from 'tsparticles';

import particlesConfig from './particles.js';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  preserveWhitespaces: true
})
export class AppComponent implements OnInit {
  title = 'frontend';

  ngOnInit(): any {
    tsParticles.load('tsparticles', particlesConfig);
  }
}
