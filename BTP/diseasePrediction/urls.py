from django.urls import path
from . import views


urlpatterns = [
    path("heartDisease/", views.heartDisease, name="heartDisease"),
    path("diabetesDisease/", views.diabetesDisease, name="diabetesDisease"),
    path("diseasePredictionResult/<str:pk>", views.diseasePredictionResult, name="diseasePredictionResult"),
    
]