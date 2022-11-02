from django.urls import path
from . import views


urlpatterns = [
    path("diseasePrediction/", views.diseasePrediction, name="diseasePrediction"),
    path("heartDisease/", views.heartDisease, name="heartDisease"),
    path("diabetesDisease/", views.diabetesDisease, name="diabetesDisease"),
    path("diseasePredictionResult/<str:pk>", views.diseasePredictionResult, name="diseasePredictionResult"),
    path("heartDiseaseInstruction/", views.heartDiseaseInstruction, name="heartDiseaseInstruction"),
    path("diabetesDiseaseInstruction/", views.diabetesDiseaseInstruction, name="diabetesDiseaseInstruction"),
    
]