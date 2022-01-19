from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def main(request):
    return render(request, 'main.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
    
def bookAppointment(request):
    return render(request, 'bookAppointment.html')
    
def about(request):
    return render(request, 'about.html')
    
def blogs(request):
    return render(request, 'blogs.html')
    
def contact(request):
    return render(request, 'contact.html')

def doctors(request):
    return render(request, 'doctors.html')

def review(request):
    return render(request, 'review.html')

def services(request):
    return render(request, 'services.html')

def login(request):
    return render(request, 'login.html')

    