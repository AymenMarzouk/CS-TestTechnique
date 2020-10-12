import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { from } from 'rxjs';
<<<<<<< HEAD
import { UserService, TestsService } from '../services';
=======
import {HistoriquetestService} from '../services/historiquetest.service'
>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6

@Component({
  selector: 'app-historiquetest',
  templateUrl: './historiquetest.component.html',
  styleUrls: ['./historiquetest.component.css']
})
export class HistoriquetestComponent implements OnInit {

  Utilisateur_Tests: any = [];
  idtest: number;
  iduser:number;

<<<<<<< HEAD
  constructor(private route: ActivatedRoute,
    private testutilisateur:UserService, 
    private testservice:TestsService,
    private router: Router) { }

  ngOnInit(): void {

=======
  constructor(private route: ActivatedRoute,private testutilisateur:HistoriquetestService, private router: Router) { }

  ngOnInit(): void {

    this.idtest = this.route.snapshot.params['id'];
>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6
    this.iduser = this.route.snapshot.params['id'];
    this.testutilisateur.getTestUtisateursById(this.iduser).subscribe((data: {}) => {
      this.Utilisateur_Tests=data
      console.log(this.Utilisateur_Tests);
  })
}

<<<<<<< HEAD
=======

>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6
gettestsbyidcategorie(id: number) {

  this.router.navigate(['/categorie', id]); 
 
}


}
