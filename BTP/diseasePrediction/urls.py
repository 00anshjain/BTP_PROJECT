from django.urls import path
from . import views


urlpatterns = [
    path("heartDisease/", views.heartDisease, name="heartDisease"),
    
]