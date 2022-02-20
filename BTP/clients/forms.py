from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class ClientProfileForm(ModelForm):
    class Meta:
        model = ClientProfile
        # fields = ['name',]
        fields = '__all__'
        exclude = ('user','name','username',)
        # exclude = ('user', 'available_time', 'qualifications')
