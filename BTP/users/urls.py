from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('bookAppointment/', views.bookAppointment, name='bookAppointment'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact, name='contact'),
    path('doctors/', views.doctors, name='doctors'),
    path('', views.index, name='index'),
    path('review/', views.review, name='review'),
    path('services/', views.services, name='services'),
    
    
]