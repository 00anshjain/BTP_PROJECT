from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Availability, Profile, Qualification


class DoctorProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)
        # exclude = ('user', 'available_time', 'qualifications')


class DoctorAvailablityForm(ModelForm):
    class Meta:
        model = Availability
        fields = '__all__'
        exclude = ('profile',)

class DoctorQualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'
        exclude = ('profile',)

    # delivery_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))


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

