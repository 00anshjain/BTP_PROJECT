from django.contrib import admin

# Register your models here.

from .models import UserOTP, TempClientProfile


admin.site.register(UserOTP)
admin.site.register(TempClientProfile)
