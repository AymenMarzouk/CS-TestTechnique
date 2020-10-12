import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AppComponent } from './app.component';
import { AlertComponent } from './components/alert.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ReactiveFormsModule } from '@angular/forms';
import { JwtInterceptor, ErrorInterceptor } from './helpers';
import { CommonModule } from '@angular/common';  
import { routing }        from './app-routing.module';
import { RouterModule } from '@angular/router';
import { ConfirmEmailComponent } from './confirm-email/confirm-email.component';
import { RegisterEntrepriseComponent } from './register-entreprise/register-entreprise.component';
import { ProfileComponent } from './profile/profile.component';
import { CategoriesComponent } from './categories/categories.component';
import { TestsComponent } from './tests/tests.component';
import { QuizComponent } from './quiz/quiz.component';
import { QuestionsService } from './services';
<<<<<<< HEAD
=======
import { FilterPipe} from './categories/filter.pipe';
>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6
import { HistoriquetestComponent } from './historiquetest/historiquetest.component';
import { ScoreComponent } from './score/score.component';

@NgModule({
  imports: [
      BrowserModule,
      ReactiveFormsModule,
      HttpClientModule,
      CommonModule,
      routing,
      RouterModule
    
  ],
  declarations: [
      AppComponent,
      AlertComponent,
      HomeComponent,
      LoginComponent,
      RegisterComponent,
      ConfirmEmailComponent,
      RegisterEntrepriseComponent,
      ProfileComponent,
      CategoriesComponent,
      TestsComponent,
      QuizComponent,
<<<<<<< HEAD
      HistoriquetestComponent,
      ScoreComponent
=======
      FilterPipe,
      HistoriquetestComponent,
      ScoreComponent 
>>>>>>> 23a3f0f1a46414cd888245a48480f0974ae079e6
     
  ],
  providers: [
      { provide: QuestionsService},
     // { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },

      // provider used to create fake backend
      //fakeBackendProvider
  ],
  bootstrap: [AppComponent]
})

export class AppModule { }