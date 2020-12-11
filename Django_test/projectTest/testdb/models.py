from django.db import models
from datetime import datetime  
# Create your models here.
class Categorie(models.Model):
    titre = models.CharField(max_length=80)
    def __str__(self):
        return self.titre

class Test(models.Model):
    titre = models.CharField(max_length=500)
    description = models.CharField(max_length=1500)
    nb_questions = models.IntegerField() 
    nb_minutes = models.IntegerField() 
    score_min =models.IntegerField(default=15) 
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

class Utilisateur(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    pwd = models.CharField(max_length=128)
    tests = models.ManyToManyField(Test, through='Utilisateur_Test')

class Utilisateur_Test(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField() 
    date = models.DateTimeField(default=datetime.now(), blank=True)
    flagechecsucces = models.IntegerField() 
    nb_reponses_correctes=models.IntegerField() 
    nb_questions_non_repondues=models.IntegerField() 
    nb_questions_repondues=models.IntegerField() 
    nb_reponse_incorrectes=models.IntegerField() 
    num_essai=models.IntegerField() 
    #duree_s = models.IntegerField() 
    #nb_reponse_correctes = models.IntegerField() 
       

class Question(models.Model):
    texte = models.CharField(max_length=1500)
    poids  = models.IntegerField(default=1) 
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

class Reponse(models.Model):
    texte = models.CharField(max_length=1500)
    reponse_correcte  = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
class Choix_Utilisateur(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    test  = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reponse = models.ForeignKey(Reponse, on_delete=models.CASCADE)
    reponse_correcte = models.IntegerField(null=True)
    class Meta:
        unique_together = (('utilisateur', 'test','question','reponse'),)

class QuestionReponse(models.Model):
    id_test =models.IntegerField()
    id_question= models.IntegerField()
    question= models.CharField(max_length=1500)
    poids  = models.IntegerField()
    id_reponse= models.IntegerField()
    reponse= models.CharField(max_length=1500)
    reponse_correctes  = models.IntegerField()