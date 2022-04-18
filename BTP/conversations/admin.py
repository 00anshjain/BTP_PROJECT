from django.contrib import admin

# Register your models here.
from .models import MessageData, Appointment

admin.site.register(MessageData)
admin.site.register(Appointment)
