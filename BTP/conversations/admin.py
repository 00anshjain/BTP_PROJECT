from django.contrib import admin

# Register your models here.
# from .models import MessageData, Appointment
from .models import *

admin.site.register(MessageData)
admin.site.register(Appointment)
admin.site.register(TempMeeting)
admin.site.register(Meeting)
