from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class DoctorProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', 'available_time', 'qualifications')


# class DoctorProfileForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'email', 'username', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super(DoctorProfileForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class':'input'})

