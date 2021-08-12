import { DOCUMENT } from '@angular/common';
import { Component, Inject } from '@angular/core';
import { AuthService } from '@auth0/auth0-angular';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { GrandprixApiService } from './grandprix-api.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  constructor(public api: GrandprixApiService,
    @Inject(DOCUMENT) public document: Document,
    public auth: AuthService) {}


  testHealthy() {
    this.api.getHealthy()
        .then(() => alert("IT WORKS!"))
        .catch((err) => alert(err.message))
  }

}
