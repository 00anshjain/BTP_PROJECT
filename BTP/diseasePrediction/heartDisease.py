from .models import DiseasePrediction, HeartDisease
from django.shortcuts import render, redirect
# from doctors.views import Profile
from doctors.models import Profile
from clients.models import ClientProfile
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import os
from django.conf import settings


# Create your views here.
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def heartDiseaseUtil(request):
    
    # loading the csv data to a Pandas DataFrame
    # heart_data = pd.read_csv('heart_disease_data.csv')
    heart_data = pd.read_csv(os.path.join(settings.DATA_ROOT, 'heart_disease_data.csv'))


    # 1 --> Defective Heart

    # 0 --> Healthy Heart

    # Splitting the Features and Target

    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']


    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    # Model Training

    # Logistic Regression

    model = LogisticRegression(max_iter=1000)

    # training the LogisticRegression model with Training data
    model.fit(X_train, Y_train)

    # accuracy on training data
    X_train_prediction = model.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

    # accuracy on test data
    X_test_prediction = model.predict(X_test)
    test_data_accuracy = accuracy_score(X_test_prediction, Y_test)


    # username = request.user.username
    profile = request.user
    try:
        prf = ClientProfile.objects.get(username=profile.username)
        isClient = True
        age = calculate_age(prf.dob)
        
    except:
        prf = Profile.objects.get(username = profile.username)
        isClient = False
        age = prf.age
    # form = HeartDiseaseForm()
    if(prf.gender == 'Male'):
        gender = 1 
    else:
        gender = 0
    

    if request.method == "POST":
        # form = HeartDiseaseForm(request.POST, instance = profile)
        # age = request.POST['age']
        # gender = request.POST['gender']
        # gender = 1
        # age = 64
        cp = int(request.POST['cp'])
        trestbps = int(request.POST['trestbps'])
        chol = int(request.POST['chol'])
        fbs = int(request.POST['fbs'])
        restecg = int(request.POST['restecg'])
        thalach = int(request.POST['thalach'])
        exang = int(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = int(request.POST['slope'])
        ca = int(request.POST['ca'])
        thal = int(request.POST['thal'])


        input_data = (age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        # input_data_as_numpy_array = np.array(input_data, dtype=float)
        # change the input data to a numpy array
        input_data_as_numpy_array= np.asarray(input_data)

        # reshape the numpy array as we are predicting for only on instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model.predict(input_data_reshaped)
        # print(prediction)

        # if (prediction[0]== 0):
        #     print('The Person does not have a Heart Disease')
        # else:
        #     print('The Person has Heart Disease')

        diseaseInstance = HeartDisease.objects.create(
            profile = profile, 
            # age = age,
            # gender = gender,
            cp = cp,
            trestbps = trestbps,
            chol = chol,
            fbs = fbs,
            restecg = restecg,
            thalach = thalach,
            exang = exang,
            oldpeak = oldpeak,
            slope = slope,
            ca = ca,
            thal = thal,
            diseaseDetected = prediction[0],
            accuracy = test_data_accuracy*100,

            
        )
        disease = DiseasePrediction.objects.create(
            profile = profile,
            testNumber = 1,
            diseaseID = diseaseInstance.heartDiseaseID,
            created = diseaseInstance.created,
        )
        print(disease)
        pk = disease.diseasePredictionID
        # print(pk)
        # print(type(pk))
        # # context = {'disease': 'Heart', 'prediction': prediction[0], 'test_data_accuracy': test_data_accuracy*100,}
        print('HI')
        print(pk)
        return redirect('diseasePredictionResult', pk)
        


    # context = {}
    # return render(request, 'diseasePrediction/heartDiseaseForm.html', context)
