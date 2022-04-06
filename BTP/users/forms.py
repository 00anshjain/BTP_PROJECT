from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.contrib.auth.models import User
# from .models import User
from django import forms

GenderChoices = (
    ("M", "Male"),
    ("F", "Female"),
)
class CustomUserCreationForm(UserCreationForm):
# This CustomUserCreationForm is inherited from UserCreationForm.
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # email = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     )
    # )
    age = forms.IntegerField()
    gender = forms.ChoiceField(
        choices=GenderChoices,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'age', 'gender', 'username', 'password1', 'password2']
        # password1 is password and password2 is renter password rfor comfirmation, Its given in django documentation
        # labels = {
        #     'first_name' : 'Name',
        # }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})







class CustomClientUserCreationForm(UserCreationForm):
    # DOB = forms.DateField()
    gender = forms.ChoiceField(
        choices=GenderChoices,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gender', 'username', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomClientUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
    
