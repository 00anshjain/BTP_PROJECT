import imp
from django.contrib import admin

# Register your models here.

from .models import HeartDisease, DiseasePrediction

admin.site.register(HeartDisease)
admin.site.register(DiseasePrediction)