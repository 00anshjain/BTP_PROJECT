from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('bookAppointment/', views.bookAppointment, name='bookAppointment'),
    path('review/', views.review, name='review'),
    path('doctorLogin/', views.doctorLogin, name='doctorLogin'),
    path("logout/", views.logoutUser, name="logout"),


]
