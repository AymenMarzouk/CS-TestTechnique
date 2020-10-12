import { Component, OnInit, OnDestroy } from '@angular/core';
import { from, Subscription } from 'rxjs';
import { first } from 'rxjs/operators';

import { User} from '../models';
<<<<<<< HEAD
=======

>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6
import { UserService, AuthenticationService, TestsService } from '../services';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import { HistoriquetestService } from '../services/historiquetest.service';

@Component({ 
    selector: 'app-home',
    templateUrl: 'home.component.html' })

export class HomeComponent implements OnInit, OnDestroy {
    currentUser: boolean;
    Utilisateur:any= [];
    currentUserSubscription: Subscription;
    users: User[] = [];
    email : string; 
    password : string ;
    constructor(
        private authenticationService: AuthenticationService,
        private userService: UserService,
        private cookieService: CookieService,
        private router: Router,
        private usertestService:HistoriquetestService
    ) {
       // this.currentUserSubscription = this.authenticationService.currentUser.subscribe(user => {
            
      //  });
    }

    ngOnInit() {
        //this.loadAllUsers();
      //  this.currentUser = this.authenticationService.currentUser;
<<<<<<< HEAD
      this.loadUtilisateurs(1);
=======
      this.loadUtilisateurs();
>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6
     
    }

    ngOnDestroy() {
        // unsubscribe to ensure no memory leaks
      // this.currentUserSubscription.unsubscribe();
    }

    deleteUser(id: number) {
        this.userService.delete(id).pipe(first()).subscribe(() => {
            this.loadAllUsers()
        });
    }

    private loadAllUsers() {
        this.userService.getAll().pipe(first()).subscribe(users => {
            this.users = users;
        });
    }

    gettestsbyiduser(iduser: number) {

        this.router.navigate(['/utilisateur_test', iduser]); 
       //  this.testservice.getTestsBycategorieId(id).subscribe((data: {}) => {
       //  this.Tests=data
      
        //})
        //return this.router.navigate(['/tests'],this.Tests); 
      }
      gettestsbyiduser1(iduser: number) {

        this.router.navigate(['/score', iduser]); 
       //  this.testservice.getTestsBycategorieId(id).subscribe((data: {}) => {
       //  this.Tests=data
      
        //})
        //return this.router.navigate(['/tests'],this.Tests); 
      }

<<<<<<< HEAD
      loadUtilisateurs(id:number) {
        return this.userService.getUsers(id).subscribe((data: {}) => {
=======
      loadUtilisateurs() {
        return this.usertestService.getUsers().subscribe((data: {}) => {
>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6
          this.Utilisateur = data;
        })
      }
}