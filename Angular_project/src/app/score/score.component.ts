import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
<<<<<<< HEAD
import { UserService } from '../services';
=======
import { HistoriquetestService } from '../services/historiquetest.service';
>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6

@Component({
  selector: 'app-score',
  templateUrl: './score.component.html',
  styleUrls: ['./score.component.css']
})
export class ScoreComponent implements OnInit {

  Utilisateur_Tests: any = [];
  Choix_Utilisateur :any =[];
  idtest: number;
  iduser:number;

<<<<<<< HEAD
  constructor(private route: ActivatedRoute,private testutilisateur:UserService, private router: Router) { }
=======
  constructor(private route: ActivatedRoute,private testutilisateur:HistoriquetestService, private router: Router) { }
>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6

  ngOnInit(): void {

    this.idtest = this.route.snapshot.params['id'];
    this.iduser = this.route.snapshot.params['id'];
    this.testutilisateur.getTestUtisateursById(this.iduser).subscribe((data: {}) => {
      this.Utilisateur_Tests=data
      console.log(this.Utilisateur_Tests);
    })
    this.testutilisateur.getChoixTestUtisateursById(this.iduser).subscribe((data:{})=>{
    this.Choix_Utilisateur=data
    console.log(this.Choix_Utilisateur);
    
  })


  }

  


<<<<<<< HEAD
}
=======
}
>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6
