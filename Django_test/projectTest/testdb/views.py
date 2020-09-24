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
from .Serializer import TestSerializer
from .Serializer import QuestionSerializer
from .Serializer import ReponseSerializer

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
        