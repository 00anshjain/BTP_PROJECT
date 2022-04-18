from django.db.models.fields import Field
from django.forms import ModelForm
from .models import Appointment
from django import forms


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "date",
            "time",
        ]


    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)

        for name, fields in self.fields.items():
            fields.widget.attrs.update({"class": "input"})

        # self.fields["title"].widget.attrs.update(
        #     {"class": "input", "placeholder": "Add Title"}
        # )
        # self.fields["description"].widget.attrs.update(
        #     {"class": "input", "placeholder": "Add Description"}
        # )
