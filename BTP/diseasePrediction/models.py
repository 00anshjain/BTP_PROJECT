from django.db import models

from clients.models import ClientProfile
# Create your models here.
from django.contrib.auth.models import User

import uuid

class HeartDisease(models.Model):
    GenderChoices = (
        ("M", "Male"),
        ("F", "Female"),
    )
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clientProfile")

    diseaseID = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
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
    


    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.profile