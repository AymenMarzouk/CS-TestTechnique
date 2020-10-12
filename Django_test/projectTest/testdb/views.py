from django.shortcuts import render
# views.py
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from .models import Categorie
from .models import Question
from .models import Choix_Utilisateur
from .Serializer import CategorieSerializer
from .models import Test
from .models import Reponse
from .models import Utilisateur_Test
from .models import Utilisateur
from .Serializer import TestSerializer
from .Serializer import QuestionSerializer
from .Serializer import UtilisateurSerializer
from .Serializer import ReponseSerializer
from .Serializer import Choix_UtilisateurSerializer
from .Serializer import Utilisateur_TestSerializer
from .Serializer import Utilisateur_TestreadSerializer

class CategorieViewSet(viewsets.ModelViewSet):  # handles GETs for many Companies

      serializer_class = CategorieSerializer
      queryset = Categorie.objects.all()
     
class TestListView(generics.ListAPIView):  # handles GETs for many Companies

      serializer_class = TestSerializer
      queryset = Test.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('categorie','id',)

class QuestionListView(generics.ListAPIView):  # handles GETs for many Companies

      serializer_class = QuestionSerializer
      queryset = Question.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('id','test',)
class ReponseListView(generics.ListAPIView):  # handles GETs for many Companies

      serializer_class = ReponseSerializer
      queryset = Reponse.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('question','reponse_correcte',)

class Choix_UtilisateurListView(generics.ListAPIView):  # handles GETs for many Companies
      serializer_class = Choix_UtilisateurSerializer
      queryset = Choix_Utilisateur.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('question',)
      def put(self, request):
        choix_utilisateur = Choix_Utilisateur.objects.filter(test=request.data['test'],utilisateur=request.data['utilisateur'],question=request.data['question'],) 
        if choix_utilisateur.exists():
            choix_utilisateur.delete()
        reponse =Reponse.objects.filter(id=request.data['reponse'])
        data=request.data
        data['reponse_correcte']=reponse[0].reponse_correcte
        serializer = Choix_UtilisateurSerializer( data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_200_OK)
class Utilisateur_TestListView(generics.ListAPIView):  

      serializer_class = Utilisateur_TestSerializer
      queryset = Utilisateur_Test.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('test','utilisateur',)
      def post(self, request):
        nb_choix_Utilisateur_all =Choix_Utilisateur.objects.filter(test=request.data['test'],utilisateur=request.data['utilisateur']).count()
        nb_choix_Utilisateur_reponse_correcte=Choix_Utilisateur.objects.filter(test=request.data['test'],utilisateur=request.data['utilisateur'],reponse_correcte=1).count()
        nb_question_all=Question.objects.filter(test=request.data['test']).count()
        nb_question_repondue=Choix_Utilisateur.objects.values('question').distinct().count()
        print('nb_choix_Utilisateur_reponse_correcte='+str(nb_choix_Utilisateur_reponse_correcte))
        print('question repondues='+str(nb_question_repondue))
        nb_question_non_repondue=nb_question_all-nb_question_repondue
        num_essai=Utilisateur_Test.objects.filter(test=request.data['test'],utilisateur=request.data['utilisateur']).count() +1
        min_score=Test.objects.filter(id=request.data['test'])[0].score_min
        score =0
        question_par_test_id=Question.objects.filter(test=request.data['test'])
        for question in question_par_test_id:
            reponses_correctes_utilisateur_par_idquestion=Choix_Utilisateur.objects.filter(question=question.id,reponse_correcte=1)
            
            reponses_correctes_par_idquestion=Reponse.objects.filter(question=question.id,reponse_correcte=1)
            i=0  
            for reponse_correcte_utilisateur in reponses_correctes_utilisateur_par_idquestion:
                  for reponse_correcte in reponses_correctes_par_idquestion:
                        if reponse_correcte_utilisateur.reponse.id == reponse_correcte.id:
                              i=i+1
            reponses_utilisateur_par_idquestion=Choix_Utilisateur.objects.filter(question=question.id)
            if i==len(reponses_utilisateur_par_idquestion) and i!=0:
                  score=score+question.poids
        poidstotal=0
        for q in question_par_test_id:
            poidstotal=poidstotal+q.poids
        scorefinal= score/poidstotal*100
        #score = nb_choix_Utilisateur_reponse_correcte/nb_choix_Utilisateur_all*100
        flagechecsucces =0
        nb_reponse_correcte=nb_choix_Utilisateur_reponse_correcte
        if scorefinal >= min_score :
            flagechecsucces=1
        data=request.data
        data['num_essai']=num_essai
        data['nb_questions_non_repondues']=nb_question_non_repondue
        data['nb_reponses_correctes']=nb_reponse_correcte
        data['nb_questions_repondues']=nb_question_repondue
        data['flagechecsucces']=flagechecsucces
        data['score']=int(scorefinal)

        print('testid='+str(request.data['test']))
        Choix_Utilisateur.objects.filter(test=request.data['test'],utilisateur=request.data['utilisateur']).delete()
        serializerUtilisateur_Test = Utilisateur_TestSerializer( data=data)
        if serializerUtilisateur_Test.is_valid():
            serializerUtilisateur_Test.save()
            return Response(serializerUtilisateur_Test.data) 
        return Response(serializerUtilisateur_Test.errors, status=status.HTTP_200_OK)

class UtilisateurListView(generics.ListAPIView):  # handles GETs for many Companies
      serializer_class = UtilisateurSerializer
      queryset = Utilisateur.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('id','firstname','lastname',)
class Utilisateur_TestreadListView(generics.ListAPIView):  
      serializer_class = Utilisateur_TestreadSerializer
      queryset = Utilisateur_Test.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('test','utilisateur',)