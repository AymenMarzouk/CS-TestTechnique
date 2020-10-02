from django.shortcuts import render
# views.py
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from .models import Categorie
from .models import Question
from .Serializer import CategorieSerializer
from .models import Test
from .models import Reponse
from .models import Utilisateur_Test
from .models import Utilisateur,Choix_Utilisateur
from .Serializer import TestSerializer
from .Serializer import QuestionSerializer
from .Serializer import ReponseSerializer
from .Serializer import Utilisateur_TestSerializer,UtilisateurSerializer,Choix_UtilisateurSerializer

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
      filter_fields = ('question',)

class Utilisateur_TestListView(generics.ListAPIView):  # handles GETs for many Companies

      serializer_class = Utilisateur_TestSerializer
      queryset = Utilisateur_Test.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('test','utilisateur',)

class UtilisateurListView(generics.ListAPIView):  # handles GETs for many Companies

      serializer_class = UtilisateurSerializer
      queryset = Utilisateur.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('id','firstname','lastname',)


class Choix_UtilisateurListView(generics.ListAPIView):  # handles GETs for many Companies
      serializer_class = Choix_UtilisateurSerializer
      queryset = Choix_Utilisateur.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields =('utilisateur', 'test','question','reponse',)
        