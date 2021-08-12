import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ManageDevelopersComponent } from './forms/manage-developers/manage-developers.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [

  { path: 'developers', component: ManageDevelopersComponent },
  { path: '', component: HomeComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
