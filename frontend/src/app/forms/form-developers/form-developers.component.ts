import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { GrandprixApiService } from 'src/app/grandprix-api.service';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-form-developers',
  templateUrl: './form-developers.component.html',
  styleUrls: ['./form-developers.component.css']
})
export class FormDevelopersComponent implements OnInit {

  constructor(public api: GrandprixApiService, public router: Router, public activeModal: NgbActiveModal) {}
  
  developer?: any

  ngOnInit(): void {
    this.developer = {
      full_name: null,
      username: null
    }
  }

  submit() {
    let api_call: Observable<any>
    api_call = this.api.createDeveloper(this.developer)
    api_call.subscribe(_ => {
      this.activeModal.close("saved")
    }, err => alert(err.message))
    
  }

}
