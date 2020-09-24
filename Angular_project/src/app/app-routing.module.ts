import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home';
import { LoginComponent } from './login';
import { RegisterComponent } from './register';
import { ProfileComponent } from './profile';
import { ConfirmEmailComponent } from './confirm-email';
import { AuthGuard } from './guards';
import { RegisterEntrepriseComponent } from './register-entreprise/register-entreprise.component';
import { CategoriesComponent } from './categories/categories.component';
import { TestsComponent } from './tests/tests.component';
import { QuizComponent } from './quiz/quiz.component';

const appRoutes: Routes = [
    { path: '', component: HomeComponent, canActivate: [AuthGuard] },
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent },
    { path: 'home', component: HomeComponent },
    { path: 'profile', component: ProfileComponent },
    { path: 'categorie', component: CategoriesComponent },
    { path: 'categorie/:id', component: TestsComponent },
    { path: 'registerentreprise', component: RegisterEntrepriseComponent },
    { path: 'quiz/:id', component: QuizComponent },
    // otherwise redirect to home
    { path: '**', redirectTo: '' }
];

export const routing = RouterModule.forRoot(appRoutes);