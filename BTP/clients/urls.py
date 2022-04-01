from django.urls import path
from . import views

urlpatterns = [
    path('clientRegister/<str:pk>/', views.clientRegister, name='clientRegister'),
]
