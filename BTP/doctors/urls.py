from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main, name='main'),
    # path('', views.main, name='main'),
    # path('services/', views.services, name='services'),
    # path('about/', views.about, name='about'),
    # path('doctors/', views.doctors, name='doctors'),
    path('doctorRegister/', views.doctorRegister, name='doctorRegister'),
    # path('contact/', views.contact, name='contact'),
    # path('bookAppointment/', views.bookAppointment, name='bookAppointment'),
    # path('review/', views.review, name='review'),
    # path('blogs/', views.blogs, name='blogs'),
    # path('login/', views.login, name='login'),
    
    
]



