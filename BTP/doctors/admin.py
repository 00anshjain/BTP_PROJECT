from django.contrib import admin

# Register your models here.
# from .models import Profile, Qualification, Availability
from .models import Profile, Qualification

admin.site.register(Profile)
admin.site.register(Qualification)
# admin.site.register(Availability)
