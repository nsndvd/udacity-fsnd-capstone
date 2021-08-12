import { Component, OnInit } from '@angular/core';
import { GrandprixApiService } from 'src/app/grandprix-api.service';

@Component({
  selector: 'app-manage-developers',
  templateUrl: './manage-developers.component.html',
  styleUrls: ['./manage-developers.component.css']
})
export class ManageDevelopersComponent implements OnInit {

  constructor(public api: GrandprixApiService) {}

  developers: any[] = []

  ngOnInit(): void {
    this.loadDevelopers()
  }

  loadDevelopers(){
    this.api.getDevelopers().subscribe(res => this.developers = res)
  }

  deleteDeveloper(id: number){
    this.api.deleteDeveloper(id).subscribe(_ => {
      this.loadDevelopers()
    })
  }

}
