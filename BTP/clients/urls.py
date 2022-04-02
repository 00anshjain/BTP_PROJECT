from django.urls import path
from . import views

urlpatterns = [
    path('clientRegister/<str:pk>/', views.clientRegister, name='clientRegister'),
    path("clientAccount/", views.clientAccount, name="clientAccount"),
    path('updateClientProfile/<str:pk>/',
         views.updateClientProfile, name='updateClientProfile'),
]
