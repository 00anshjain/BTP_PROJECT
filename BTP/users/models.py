from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from django.http import request


import uuid


class UserOTP(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.SmallIntegerField()


class TempClientProfile(models.Model):
    GenderChoices = (
        ("M", "Male"),
        ("F", "Female"),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null = True, blank = True)
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    # ANytime user is deleted the profile is deleted
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GenderChoices, blank=False, null=False)
    dob = models.DateField()
    username = models.CharField(max_length=200, blank=True, null=True)
    TempCid = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class TempDoctorProfile(models.Model):
    GenderChoices = (
        ("M", "Male"),
        ("F", "Female"),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null = True, blank = True)
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    # ANytime user is deleted the profile is deleted
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GenderChoices, blank=False, null=False)
    age = models.IntegerField(null=False)
    username = models.CharField(max_length=200, blank=True, null=True)
    TempDid = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

