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
from rest_framework.views import APIView
from .models import Categorie
from .models import Question
from .models import Choix_Utilisateur
from .Serializer import CategorieSerializer
from .models import Test
from .models import Reponse
from .models import Utilisateur_Test
from .models import Utilisateur
from .models import QuestionReponse
from .Serializer import TestSerializer,TestcreateSerializer
from .Serializer import QuestionSerializer
from .Serializer import UtilisateurSerializer
from .Serializer import ReponseSerializer
from .Serializer import Choix_UtilisateurSerializer
from .Serializer import Utilisateur_TestSerializer
from .Serializer import Utilisateur_TestreadSerializer
from .Serializer import QuestionReponseSerializer
from xlrd import open_workbook
import  simplejson



class CategorieViewSet(viewsets.ModelViewSet):  # handles GETs for many Companies

      serializer_class = CategorieSerializer
      queryset = Categorie.objects.all()
     
class TestListView(generics.ListAPIView):  # handles GETs for many Companies

      serializer_class = TestSerializer
      queryset = Test.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('categorie','id',)

class TestCreateView(generics.CreateAPIView):  # handles GETs for many Companies

      serializer_class = TestcreateSerializer
      queryset = Test.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('categorie','id',)



class QuestionListView(generics.ListCreateAPIView):  # handles GETs for many Companies

      serializer_class = QuestionSerializer
      queryset = Question.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('test','id',)
class ReponseListView(generics.ListCreateAPIView):  # handles GETs for many Companies

      serializer_class = ReponseSerializer
      queryset = Reponse.objects.all()
      filter_backends=(DjangoFilterBackend,)
      filter_fields = ('question','reponse_correcte',)

class QuestionReponseView(APIView):

      def post(self, request, format=None):
          
        response=[]
        for reponse in request.data:
            reponse_correcte = reponse.get("reponse_correcte")
            texte = reponse.get("texte")
            question = reponse['question']['id']
            data = {'reponse_correcte': reponse_correcte,'texte': texte, 'question': question}
            serializer = ReponseSerializer(data=data)
            if serializer.is_valid():
                  serializer.save()
                  response.append(reponse) 
                  
        return Response(response, status=status.HTTP_200_OK)

class ReponseCreateView (generics.CreateAPIView):
   def post(self,request, format=None):
       file_obj = request.FILES['file']
    
       wb = open_workbook(file_contents=file_obj.read())
       sh=wb.sheet_by_index(1)
       
       values = []
       responses=[]
       
       for row in range(1,sh.nrows): 
              col_names = sh.row(1)
              col_value = []
              for name, col in zip(col_names, range(sh.ncols)):
                  value  = (sh.cell(row,col).value)
                  
                  try : value = str(int(value))
                  except : pass
                  col_value.append((value))
              values.append(col_value)
              print (values)
            
              text = sh.cell_value(row,1)
              reponse_correcte = sh.cell_value(row,2)
              question = sh.cell_value(row,3)
              print(text)
              data = {'texte': text ,'reponse_correcte': reponse_correcte, 'question':  int(question) }
            
              serializer = ReponseSerializer(data=data)
              if serializer.is_valid():
                  serializer.save()
                  responses.append(serializer.data)
            
                  
       return Response(responses, status=status.HTTP_200_OK) 
   



class QuestionCreateView(generics.CreateAPIView):

 def post(self,request, format=None):
    file_obj = request.FILES['file']
    
    wb = open_workbook(file_contents=file_obj.read())
    
    values = []
    questions=[]
    for s in wb.sheets():
      #print 'Sheet:',s.name
        for row in range(1, s.nrows):
             
            col_names = s.row(0)
            col_value = []
            for name, col in zip(col_names, range(s.ncols)):
                  value  = (s.cell(row,col).value)
                  
                  try : value = str(int(value))
                  except : pass
                  col_value.append((value))
            values.append(col_value)
            print (values)
            
            text = s.cell_value(row,0)
            poids = s.cell_value(row,1)
            test = s.cell_value(row,2)
            print(text)
            data = {'texte': text ,'poids': str(poids), 'test':  int(test) }
            
            serializer = QuestionSerializer(data=data)
            if serializer.is_valid():
                  serializer.save()
                  questions.append(serializer.data)
            
                  
    return Response(questions, status=status.HTTP_200_OK)
    
                  
    
class QuestionReponseCreateView(generics.CreateAPIView):

 def post(self,request, format=None):
    file_obj = request.FILES['file']
    
    wb = open_workbook(file_contents=file_obj.read())
    
    values = []
    questionreponses=[]
    for s in wb.sheets():
      #print 'Sheet:',s.name
        for row in range(1, s.nrows):
             
            col_names = s.row(0)
            col_value = []
            for name, col in zip(col_names, range(s.ncols)):
                  value  = (s.cell(row,col).value)
                  
                  try : value = str(int(value))
                  except : pass
                  col_value.append((value))
            values.append(col_value)
            print (values)
            id_test = s.cell_value(row,0)
            id_question = s.cell_value(row,1)
            question = s.cell_value(row,2)
            poids= s.cell_value(row,3)
            id_reponse = s.cell_value(row,4)
            reponse = s.cell_value(row,5)
            reponse_correcte= s.cell_value(row,6)
            nb_question_repondue=QuestionReponse.objects.values('question').distinct()
            data = { 'question':  question ,'poids': str(poids),'reponse': reponse,'reponse_correctes': str(reponse_correcte),
            'id_question': str(id_question),'id_reponse': str(id_reponse ),'id_test': str(id_test )}

            #queryset  = QuestionReponse.objects.raw(" select distinct id ,id_test , id_question ,question , id_reponse from public.testdb_questionreponse ")
            #queryset1 = self.get_queryset ()
            #print(result)
            #serializer = QuestionReponseSerializer(list(queryset1))
            #dataquestion=data = { 'question':  question ,'reponse': reponse ,'id_question': int(id_question),'id_reponse':  int(id_reponse) ,'id_test': int(id_test) ,}
            #serializerquestion=QuestionSerializer(data=dataquestion)
            #if(serializerquestion.is_valid()):
                  #serializerquestion.save()
                  
            serializer = QuestionReponseSerializer(data=data)
            if serializer.is_valid():
                  serializer.save()
                  questionreponses.append(serializer.data)
            
                  
    return Response(questionreponses, status=status.HTTP_200_OK)




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
        nb_reponse_incorrectes=Choix_Utilisateur.objects.filter(test=request.data['test'],utilisateur=request.data['utilisateur'],reponse_correcte=0).count()
        if scorefinal >= min_score :
            flagechecsucces=1
        data=request.data
        data['num_essai']=num_essai
        data['nb_questions_non_repondues']=nb_question_non_repondue
        data['nb_reponses_correctes']=nb_reponse_correcte
        data['nb_questions_repondues']=nb_question_repondue
        data['flagechecsucces']=flagechecsucces
        data['score']=int(scorefinal)
        data['nb_reponse_incorrectes']=nb_reponse_incorrectes

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