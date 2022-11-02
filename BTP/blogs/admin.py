from django.contrib import admin

# Register your models here.

from .models import Blog, Tag, Review

admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Review)

