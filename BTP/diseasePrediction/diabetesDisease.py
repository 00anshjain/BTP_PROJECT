from .models import DiseasePrediction, DiabetesDisease
from django.shortcuts import render, redirect
# from doctors.views import Profile
from doctors.models import Profile
from clients.models import ClientProfile

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


import os
from django.conf import settings


# Create your views here.
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv(os.path.join(settings.DATA_ROOT, 'diabetes.csv'))

def diabetesDiseaseUtil(request):

  # separating the data and labels
  X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
  Y = diabetes_dataset['Outcome']

  scaler = StandardScaler()
  scaler.fit(X)
  standardized_data = scaler.transform(X)

  X = standardized_data
  Y = diabetes_dataset['Outcome']

  X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)

  classifier = svm.SVC(kernel='linear')
  #training the support vector Machine Classifier
  classifier.fit(X_train, Y_train)

  # accuracy score on the training data
  X_train_prediction = classifier.predict(X_train)
  training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

  # accuracy score on the test data
  X_test_prediction = classifier.predict(X_test)
  test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

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
    pregnancies = int(request.POST['pregnancies'])
    glucose = int(request.POST['glucose'])
    bloodPressure = int(request.POST['bloodPressure'])
    skinThickness = int(request.POST['skinThickness'])
    insulin = int(request.POST['insulin'])
    BMI = float(request.POST['BMI'])
    diabetesPedigreeFunction = float(request.POST['diabetesPedigreeFunction'])


    

    input_data = (pregnancies,glucose,bloodPressure,skinThickness,insulin,BMI,diabetesPedigreeFunction,age)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the input data
    std_data = scaler.transform(input_data_reshaped)
    # print(std_data)

    prediction = classifier.predict(std_data)
    # print(prediction)

    # if (prediction[0] == 0):
    #   print('The person is not diabetic')
    # else:
    #   print('The person is diabetic')

    diseaseInstance = DiabetesDisease.objects.create(
      profile = profile, 
      # age = age,
      # gender = gender,
      pregnancies = pregnancies,
      glucose = glucose,
      bloodPressure = bloodPressure,
      skinThickness = skinThickness,
      insulin = insulin,
      BMI = BMI,
      diabetesPedigreeFunction = diabetesPedigreeFunction,
      diseaseDetected = prediction[0],
      accuracy = test_data_accuracy*100,

      
  )
  disease = DiseasePrediction.objects.create(
      profile = profile,
      testNumber = 2,
      diseaseID = diseaseInstance.diabetesDiseaseID,
      created = diseaseInstance.created,
  )
  print(disease)
  pk = disease.diseasePredictionID
  # print(pk)
  # print(type(pk))
  # # context = {'disease': 'Heart', 'prediction': prediction[0], 'test_data_accuracy': test_data_accuracy*100,}
  # print('HI')
  # print(pk)
  return redirect('diseasePredictionResult', pk)

    
