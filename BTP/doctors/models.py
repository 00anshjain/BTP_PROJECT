from django.db import models
from django.contrib.auth.models import User  # user used by django for authetication and login in admin page
# check django user model for more information
# Create your models here.
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from phone_field import PhoneField

# from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    # ANytime user is deleted the profile is deleted
    name = models.CharField(max_length=200, blank = True, null = True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    available_time = models.OneToOneField('Availability', on_delete=models.CASCADE, null = True, blank = True)
    qualifications = models.ManyToManyField('Qualification', blank = True)
    username = models.CharField(max_length=200, blank = True, null = True)
    location = models.CharField(max_length=500, blank = True, null = True)
    short_intro = models.CharField(max_length=200, blank = True, null = True)
    bio = models.TextField(blank = True, null = True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    speciality = models.CharField(max_length=200, blank = True, null = True)
    contact_number = PhoneField(blank=True, help_text='Contact phone number')

    # We want specifically a folder for profile pictures. SO in static in mages we create a new folder here
    # static->images->profiles
    # social_github = models.CharField(max_length=200, blank = True, null = True)
    # social_twitter = models.CharField(max_length=200, blank = True, null = True)
    # social_linkedin = models.CharField(max_length=200, blank = True, null = True)
    # social_youtube = models.CharField(max_length=200, blank = True, null = True)
    # social_website = models.CharField(max_length=200, blank = True, null = True)
    joining_date = models.DateField(auto_now_add = True)
    Did = models.UUIDField(default=uuid.uuid4, unique=True, primary_key = True, editable = False)
    

    def __str__(self):
        return str(self.username)

class Qualification(models.Model):
    degree_name = models.CharField(max_length =200)
    degree_date = models.DateField()
    university = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key = True, editable = False)
    # id = models.UUIDField(default=generateUUID, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.name


class Availability(models.Model):
    monday_from = models.DateTimeField(null = True, blank = True)
    monday_to = models.DateTimeField(null = True, blank = True)
    tuesday_from = models.DateTimeField(null = True, blank = True)
    tuesday_to = models.DateTimeField(null = True, blank = True)
    wednesday_from = models.DateTimeField(null = True, blank = True)
    wednesday_to = models.DateTimeField(null = True, blank = True)
    thursday_from = models.DateTimeField(null = True, blank = True)
    thursday_to = models.DateTimeField(null = True, blank = True)
    friday_from = models.DateTimeField(null = True, blank = True)
    friday_to = models.DateTimeField(null = True, blank = True)
    saturday_from = models.DateTimeField(null = True, blank = True)
    saturday_to = models.DateTimeField(null = True, blank = True)
    sunday_from = models.DateTimeField(null = True, blank = True)
    sunday_to = models.DateTimeField(null = True, blank = True)
    
    