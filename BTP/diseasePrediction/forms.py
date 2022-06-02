from django.db.models.fields import Field
from django.forms import ModelForm
from django import forms
from .models import HeartDisease



class HeartDiseaseForm(ModelForm):
    class Meta:
        model = HeartDisease
        fields = '__all__'
        exclude = ('age', 'gender', 'profile',)


    def __init__(self, *args, **kwargs):
        super(HeartDiseaseForm, self).__init__(*args, **kwargs)

        for name, fields in self.fields.items():
            fields.widget.attrs.update({"class": "input"})

        # self.fields["title"].widget.attrs.update(
        #     {"class": "input", "placeholder": "Add Title"}
        # )
        # self.fields["description"].widget.attrs.update(
        #     {"class": "input", "placeholder": "Add Description"}
        # )
