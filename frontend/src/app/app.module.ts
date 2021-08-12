import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AuthModule, AuthHttpInterceptor } from '@auth0/auth0-angular';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormResourcesComponent } from './forms/form-resources/form-resources.component';
import { FormDevelopersComponent } from './forms/form-developers/form-developers.component';
import { HomeComponent } from './home/home.component';
import { FormsModule } from '@angular/forms';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ManageDevelopersComponent } from './forms/manage-developers/manage-developers.component';

@NgModule({
  declarations: [
    AppComponent,
    FormResourcesComponent,
    FormDevelopersComponent,
    HomeComponent,
    ManageDevelopersComponent
  ],
  imports: [
    BrowserModule,
    AuthModule.forRoot({
      domain: 'nsndvd.eu.auth0.com',
      clientId: 'ttMrqpym89t5HC5oiA93YYvoi2XFXoyM',
      audience: 'nsndvd-ucs-api',
      callbackURL: 'http://localhost:4200',
      httpInterceptor: {
        allowedList: [
          // Attach access tokens to any calls
          '/*',
          '*'
        ]
      },
    }),
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    NgbModule
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthHttpInterceptor, multi: true },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
