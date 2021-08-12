import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { map, tap } from 'rxjs/operators';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class GrandprixApiService {

  constructor(private http: HttpClient) { }
  path = environment.backend
  
  getHealthy(): Promise<boolean> {
    return this.http.get(`${this.path}/healthy`)
      .pipe(tap(res => console.log(res), err => console.log(err)))
      .pipe(map((res: any) => res.healthy))
      .toPromise() as any
  }

  getDashboard(): Observable<any> {
    return this.http.get(`${this.path}/dashboard`)
  }


  getResources(): Observable<any> {
    return this.http.get(`${this.path}/resources`)
  }

  editResource(id: number, body: any): Observable<any> { 
    return this.http.patch(`${this.path}/resources/${id}`, body) 
  }

  deleteResource(id: number): Observable<any> {
    return this.http.delete(`${this.path}/resources/${id}`)
  }

  createResource(body: any): Observable<any> {
    return this.http.post(`${this.path}/resources`, body)
  }


  getDevelopers(): Observable<any> {
    return this.http.get(`${this.path}/developers`)
  }

  deleteDeveloper(id: number): Observable<any> {
    return this.http.delete(`${this.path}/developers/${id}`)
  }

  createDeveloper(body: any): Observable<any> {
    return this.http.post(`${this.path}/developers`, body)
  }


  createBooking(body: any): Observable<any> {
    return this.http.post(`${this.path}/bookings`, body)
  }

  deleteBooking(id: number): Observable<any> {
    return this.http.delete(`${this.path}/bookings/${id}`)
  }
}
