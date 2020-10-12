import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Utilisateur_Test } from  '../models/Utilisateur_test';
import { Utilisateur} from  '../models/Utilisateur';
import {Choix_Utilisateur} from '../models/Choix_Utilisateur';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class HistoriquetestService {

    // Define API
    apiURL = 'http://localhost:8000';

    constructor(private http: HttpClient) { }
  
    /*========================================
      CRUD Methods for consuming RESTful API
    =========================================*/
  
    // Http Options
    httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    } 



  getTestUtisateursById(iduser): Observable<Utilisateur_Test> {
    return this.http.get<Utilisateur_Test>(this.apiURL + '/utilisateur_test?utilisateur='+ iduser)
    .pipe(
      catchError(this.handleError)
    )
  }

  getChoixTestUtisateursById(iduser): Observable<Choix_Utilisateur> {
    return this.http.get<Choix_Utilisateur>(this.apiURL + '/choix_utilisateur_test?utilisateur='+ iduser)
    .pipe(
      catchError(this.handleError)
    )
  }

  getUsers(): Observable<Utilisateur> {
    return this.http.get<Utilisateur>(this.apiURL + '/users')
    .pipe(
      catchError(this.handleError)
    )
  }

    // Error handling 
    handleError(error) {
      let errorMessage = '';
      if(error.error instanceof ErrorEvent) {
        // Get client-side error
        errorMessage = error.error.message;
      } else {
        // Get server-side error
        errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
      }
      window.alert(errorMessage);
      return throwError(errorMessage);
   }
}
