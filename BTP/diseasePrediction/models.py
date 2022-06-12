from django.db import models

from clients.models import ClientProfile
# Create your models here.
from django.contrib.auth.models import User
import datetime
import uuid


class DiseasePrediction(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="DiseasePredictionProfile")
    diseasePredictionID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    testNumber = models.IntegerField(null=False, blank=False)
    diseaseID = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now)
    # diseaseID = 1 for HeartDiseasePrediction
    # diseaseID = 2 for DiabetesDiseasePrediction
    
    def __str__(self):
        return 'TestID: ' + str(self.testNumber) +',  ' + self.profile.username
        # return self.profile.username + " " + self.testNumber
        

class DiabetesDisease(models.Model):
    GenderChoices = (
        ("M", "Male"),
        ("F", "Female"),
    )
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="diabetesDiseasePatient")

    diabetesDiseaseID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    pregnancies = models.PositiveIntegerField(null=False)
    glucose = models.PositiveIntegerField(null=False)
    bloodPressure = models.PositiveIntegerField(null=False)
    skinThickness = models.PositiveIntegerField(null=False)
    insulin = models.PositiveIntegerField(null=False)
    BMI = models.FloatField(null=False)
    diabetesPedigreeFunction = models.FloatField(null=False)


    diseaseDetected = models.IntegerField(default=-1)   # -1 result not predicted till now by the model
    accuracy = models.FloatField(null=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.profile.username


class HeartDisease(models.Model):
    GenderChoices = (
        ("M", "Male"),
        ("F", "Female"),
    )
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="heartDiseasePatient")

    heartDiseaseID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    # age = models.PositiveIntegerField(null=False)
    # gender = models.CharField(
    #     max_length=1, choices=GenderChoices, blank=False, null=False)
    cp = models.PositiveIntegerField(null=False)
    trestbps = models.PositiveIntegerField(null=False)
    chol = models.PositiveIntegerField(null=False)
    fbs = models.PositiveIntegerField(null=False)
    restecg = models.PositiveIntegerField(null=False)
    thalach = models.PositiveIntegerField(null=False)
    exang = models.PositiveIntegerField(null=False)
    oldpeak = models.FloatField(null=False)
    slope = models.PositiveIntegerField(null=False)
    ca = models.PositiveIntegerField(null=False)
    thal = models.PositiveIntegerField(null=False)
    diseaseDetected = models.IntegerField(default=-1)   # -1 result not predicted till now by the model
    accuracy = models.FloatField(null=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.profile.username