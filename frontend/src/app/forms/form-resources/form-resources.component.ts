import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { GrandprixApiService } from 'src/app/grandprix-api.service';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-form-resources',
  templateUrl: './form-resources.component.html',
  styleUrls: ['./form-resources.component.css']
})
export class FormResourcesComponent implements OnInit {

  constructor(public api: GrandprixApiService, public router: Router, public activeModal: NgbActiveModal) {}
  
  @Input('resource')
  resource?: any
  new_resource = false

  ngOnInit(): void {
    if (!this.resource) {
      this.new_resource = true
      this.resource = {
        name: null,
        note: null,
        img_url: null
      }
    }
  }

  submit() {
    let api_call: Observable<any>
    if (this.new_resource) {
      api_call = this.api.createResource(this.resource)
    } else {
      api_call = this.api.editResource(this.resource.id, this.resource)
    }
    api_call.subscribe(_ => {
      this.activeModal.close("saved")
    }, err => alert(err.message))
    
  }

}
