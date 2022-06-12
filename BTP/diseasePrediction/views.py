
from doctors.views import Profile
from doctors.models import *
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *
from doctors.models import Profile

from django.core.mail import send_mail
from django.conf import settings
# from django.db.models import Q

# import jwt
import requests
import json
from time import time

import requests
import json
from datetime import datetime, timedelta
# import pytz

from .heartDisease import heartDiseaseUtil
from .diabetesDisease import diabetesDiseaseUtil

def diseasePrediction(request):
    return render(request, 'diseasePrediction/diseasePrediction.html')

def heartDisease(request):
    if request.method == 'POST':
        return heartDiseaseUtil(request)
    context = {}
    return render(request, 'diseasePrediction/heartDiseaseForm.html', context)

def diabetesDisease(request):
    if request.method == 'POST':
        return diabetesDiseaseUtil(request)
    context = {}
    return render(request, 'diseasePrediction/diabetesDiseaseForm.html', context)



def diseasePredictionResult(request, pk):
    diseasePrediction = DiseasePrediction.objects.get(diseasePredictionID=pk)
    testNumber = diseasePrediction.testNumber
    if testNumber == 1:
        disease = HeartDisease.objects.get(heartDiseaseID = diseasePrediction.diseaseID)
        speciality = 'Cardio'
        diseaseName = 'Heart Disease'
    if testNumber == 2:
        disease = DiabetesDisease.objects.get(diabetesDiseaseID = diseasePrediction.diseaseID)
        speciality = 'Diabetes'
        diseaseName = 'Diabetes Disease'
    
    result = disease.diseaseDetected
    accuracy = int(disease.accuracy)    
    doctorList = Profile.objects.filter(
        Q(speciality__icontains=speciality))
    print(doctorList)
    context = {'result' : result, 'accuracy' : accuracy, 'speciality' : speciality, 'diseaseName' : diseaseName, 'doctorList' :doctorList}
    return render(request, 'diseasePrediction/diseasePredictionResult.html', context)