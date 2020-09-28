# serializers.py
from rest_framework.serializers import ModelSerializer

from .models import Categorie
from .models import Test
from .models import Utilisateur
from .models import Question
from .models import Utilisateur_Test
from .models import Choix_Utilisateur
from .models import Reponse
class CategorieSerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = (
            'id', 'titre'
        )
class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = (
            'id', 'titre', 'description', 'nb_questions', 'nb_minutes', 'categorie'
        )
        depth=1
class UtilisateurSerializer(ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = (
            'id', 'firstname', 'lastname', 'email', 'pwd', 'tests'
        )
class Utilisateur_TestSerializer(ModelSerializer):
    class Meta:
        model = Utilisateur_Test
        fields = (
            'id','utilisateur', 'test', 'score'
        )
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
            'id','utilisateur', 'test', 'question', 'reponse'
        )