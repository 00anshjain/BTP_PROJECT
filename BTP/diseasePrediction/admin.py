import imp
from django.contrib import admin

# Register your models here.

from .models import HeartDisease

admin.site.register(HeartDisease)