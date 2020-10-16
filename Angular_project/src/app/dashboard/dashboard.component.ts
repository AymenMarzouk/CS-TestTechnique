import { Component, OnInit } from '@angular/core';
import { ChartDataSets, ChartOptions, ChartType } from 'chart.js';
/*import * as pluginDataLabels from 'chartjs-plugin-datalabels';*/
import { Label } from 'ng2-charts';
import { UtilisateurTestService } from '../services/utilisateur-test.service';
/*import { Chart } from 'chart.js';*/
import { UtilisateurTest } from '../models/UtilisateurTest';
import { HttpClient } from '@angular/common/http';
import { timestamp } from 'rxjs/operators';
import {Chart} from 'node_modules/chart.js';



@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  public canvas: any;
  utilisateurtest: UtilisateurTest[];
  chart = [];
  test =[];
  score = [];
  reponse=[];
  chart1 =[];
  chart2 =[];
  chart3 =[];
  url = 'http://localhost:8000/utilisateur_test';
  constructor(private utilisateurtestService: UtilisateurTestService,private httpClient: HttpClient) {}

  ngOnInit()  {
    
    
    this.httpClient.get(this.url).subscribe((res: UtilisateurTest[]) => {
    /*this.utilisateurtestService.GetUtilisateurTest().subscribe((res: UtilisateurTest[]) => {*/
     res.forEach(y => {
        this.test.push(y.test);
        
        console.log(res)
        this.score.push(y.score);
        this.reponse.push(y.nb_reponses_correctes);
       
     
      });

      
      
      this.chart = new Chart('canvas', {
        type: 'bar',
        data: {
          labels: this.test ,
          
          datasets: [
            {
              data:this.score,
             label:'Score',
              borderColor: '#33FFBB ',
             backgroundColor:'#33FFBB',
              fill: true
             
              
            },
           {
              data:this.reponse,
              label:'Reponse Correcte',
               borderColor: '#FBA3EB',
              backgroundColor:'#FBA3EB',
               fill: false,
               
               
            }
          ],
          
          
        },
        options: {
          legend: {
            display: true,
            
          },
          scales: {
            xAxes: [{
              display: true
            }],
            yAxes: [{
              display: true
            }],
          }
        }
      });

      this.chart1 = new Chart('canvas1', {
        type: 'line',
        data: {
          labels: this.test,
          
          
          datasets: [
            {
              data:this.score,
             label:'Score',
              borderColor: '#A3D4FB ',
              backgroundColor:'#A3D4FB ',
              fill: false
             
              
            },
           {
              data:this.reponse,
              label:'Reponse Correcte',
               borderColor: '#FAFBA3',
               backgroundColor:'#FAFBA3',
               fill: false,
               
               
            }
          ],
          
          
        },
        options: {
          legend: {
            display: true,
            
          },
          
        }
      });


      this.chart2 = new Chart('canvas2', {
        type: 'polarArea',
        data: {
          labels: this.test ,
          
          datasets: [
            {
              data:this.reponse,
             label:'Reponse correcte',
              borderColor: '#FD786B ',
             /*backgroundColor:'#FD786B ',*/
              fill: false
             
              
            }
           
          ],
          
          
        },
        options: {
          legend: {
            display: true,
            
          },
          scales: {
            xAxes: [{
              display: true
            }],
            yAxes: [{
              display: true
            }],
          }
        }
      });
      
      
      this.chart3 = new Chart('canvas3', {
        type: 'bar',
        data: {
          labels: this.test ,
          
          datasets: [
            {
              data:this.score,
             label:'Score',
              borderColor: '#71F963 ',
             backgroundColor:'#71F963',
              fill: true
             
              
            },
           
          ],
          
          
        },
        options: {
          legend: {
            display: true,
            
          },
          scales: {
            xAxes: [{
              display: true
            }],
            yAxes: [{
              display: true
            }],
          }
        }
      });

    });
  



    
    
   
  }
  
 

  
}
