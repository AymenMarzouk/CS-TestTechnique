# serializers.py
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Categorie
from .models import Test
from .models import Utilisateur
from .models import Question
from .models import Utilisateur_Test
from .models import Choix_Utilisateur
from .models import Reponse
class CategorieSerializer(ModelSerializer):
    


    total_test = serializers.SerializerMethodField(read_only=True)

    def get_total_test(self, categorie):
        return categorie.test_set.count() # change 'test' with corresponding "related_name" value

    class Meta:
        model = Categorie
        fields = (
            'id', 'titre','total_test'
        )
class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = (
            'id', 'titre', 'description', 'nb_questions', 'nb_minutes', 'categorie'
        )
class UtilisateurSerializer(ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = (
            'id', 'firstname', 'lastname', 'email', 'pwd', 'tests'
        )
        depth = 1
class Utilisateur_TestSerializer(ModelSerializer):
    class Meta:
        model = Utilisateur_Test
        fields = (
            'id','utilisateur', 'test', 'score','date','flagechecsucces','nb_reponses_correctes','nb_questions_non_repondues','nb_questions_repondues','nb_reponse_incorrectes','num_essai'
        )
class Utilisateur_TestreadSerializer(ModelSerializer):
    class Meta:
        model = Utilisateur_Test
        fields = (
            'id','utilisateur', 'test', 'score','date','flagechecsucces','nb_reponses_correctes','nb_questions_non_repondues','nb_questions_repondues','nb_reponse_incorrectes','num_essai'
        )
        depth=1
class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id', 'texte', 'poids', 'test'
        )
class ReponseSerializer(ModelSerializer):
    class Meta:
        model = Reponse
        fields = (
            'id', 'texte', 'reponse_correcte', 'question'
        )
class Choix_UtilisateurSerializer(ModelSerializer):
    class Meta:
        model = Choix_Utilisateur
        fields = (
            'id','utilisateur', 'test', 'question', 'reponse','reponse_correcte'
        )