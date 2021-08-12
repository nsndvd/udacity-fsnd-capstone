import { Component, Inject, OnInit } from '@angular/core';
import { GrandprixApiService } from '../grandprix-api.service';
import { AuthService } from '@auth0/auth0-angular';
import { DOCUMENT } from '@angular/common';
import { JwtHelperService } from "@auth0/angular-jwt";
import { of } from 'rxjs';
import { map, switchMap, take } from 'rxjs/operators';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormResourcesComponent } from '../forms/form-resources/form-resources.component';
import { FormDevelopersComponent } from '../forms/form-developers/form-developers.component';



@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{
  
  constructor(public api: GrandprixApiService,
              @Inject(DOCUMENT) public document: Document,
              public auth: AuthService,
              public router: Router,
              private modalService: NgbModal) {}
  
  helper = new JwtHelperService();
  title = 'Grandprix';
  dashboard: any[] = [];
  
  permissions$ = this.auth.isAuthenticated$
      .pipe(switchMap(is_authenticated => {
        if (!is_authenticated) {
          return of([])
        } else {
          return this.auth.getAccessTokenSilently()
            .pipe(map(access_token => {
              console.log(access_token)
              console.log(this.helper.decodeToken(access_token))
              return this.helper.decodeToken(access_token).permissions
            }))
        }}))

  ngOnInit() {
    this.auth.isAuthenticated$.subscribe(isAuthenticated => {
      if (!isAuthenticated) {
        this.dashboard = []
      } else {
        this.loadDashboard()
      }
    })
  }

  loadDashboard() {
    this.api.getDashboard().subscribe(res => this.dashboard = res)
  }
  
  deleteResource(id: number) {
    this.api.deleteResource(id).subscribe(_ => this.loadDashboard(), err =>  alert(err.message))
  }

  deleteBooking(id: number) {
    this.api.deleteBooking(id).subscribe(_ => this.loadDashboard(), err =>  alert(err.message))
  }

  editResource(resource: any) {
    let modalRef = this.modalService.open(FormResourcesComponent)
    modalRef.componentInstance.resource = resource
    modalRef.closed.subscribe(result => {
      if (result == 'saved') { 
        this.loadDashboard()
      }})
  }

  createDeveloper() {
    let modalRef = this.modalService.open(FormDevelopersComponent)
    modalRef.closed.subscribe(result => {
      if (result == 'saved') {
        this.router.navigate(['developers'])
      }})
  }

  reserve(resource: any) {
    this.api.createBooking({
      resource_id: resource.id,
      expected_duration_hours: 1
    }).subscribe(_ => {
      this.loadDashboard()
    }, err => {
      alert(err.message)
    })
  }

}
