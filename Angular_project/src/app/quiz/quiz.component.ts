import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { TestsService,QuestionsService, ReponsesService } from '../services';
import { Question } from '../models/Question';
@Component({
  selector: 'app-quiz',
  templateUrl: './quiz.component.html',
  styleUrls: ['./quiz.component.css']
})
export class QuizComponent implements OnInit {
  beforeQ =true;
  compteurQuestion=0
  Questions: any = [];
  Reponses: any =[];
  Tests: any = [];
  id: number;
  idquestion:  number;
  constructor(
    private testservice: TestsService,
    private route: ActivatedRoute,
    private questionservice: QuestionsService,
    private reponseservice: ReponsesService,
  ) { }

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];
    this.testservice.getTestsById(this.id).subscribe((data: {}) => {
      this.Tests=data
  })
  }
  passertest(){
    this.beforeQ =false;
    this.questionservice.getQuestionsBytestId(this.id).subscribe((data: {}) => {
      this.Questions=data
      this.idquestion = this.Questions[this.compteurQuestion]['id'];
      console.log(this.idquestion)
      this.reponseservice.getReponsesByQuestionId(this.idquestion).subscribe((data: {}) => {
        this.Reponses=data
       console.log(this.Reponses)
    })
    this.compteurQuestion++;
  })

  }
}
