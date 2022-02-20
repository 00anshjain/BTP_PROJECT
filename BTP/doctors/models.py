from django.db import models
# user used by django for authetication and login in admin page
from django.contrib.auth.models import User
# check django user model for more information
# Create your models here.
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from phone_field import PhoneField
import datetime

# from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    GenderChoices = (
        ("M", "Male"),
        ("F", "Female"),
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    # ANytime user is deleted the profile is deleted
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GenderChoices, blank=False, null=False)
    age = models.IntegerField(null=False)
    # available_time = models.OneToOneField(
    # 'Availability', on_delete=models.CASCADE, null=True, blank=True)
    # qualifications = models.ManyToManyField('Qualification', blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    speciality = models.CharField(max_length=200, blank=True, null=True)
    contact_number = PhoneField(blank=True, help_text='Contact phone number')

    # We want specifically a folder for profile pictures. SO in static in mages we create a new folder here
    # static->images->profiles
    # social_github = models.CharField(max_length=200, blank = True, null = True)
    # social_twitter = models.CharField(max_length=200, blank = True, null = True)
    # social_linkedin = models.CharField(max_length=200, blank = True, null = True)
    # social_youtube = models.CharField(max_length=200, blank = True, null = True)
    # social_website = models.CharField(max_length=200, blank = True, null = True)
    joining_date = models.DateField(auto_now_add=True)
    Did = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class Qualification(models.Model):
    degree_name = models.CharField(max_length=200)
    degree_date = models.DateField()
    university = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # id = models.UUIDField(default=generateUUID, unique=True, primary_key = True, editable = False)

    def __str__(self):
        return self.degree_name


class Availability(models.Model):
    monday_from = models.TimeField(default=datetime.time(16, 00))
    monday_to = models.TimeField(default=datetime.time(16, 00))
    tuesday_from = models.TimeField(default=datetime.time(16, 00))
    tuesday_to = models.TimeField(default=datetime.time(16, 00))
    wednesday_from = models.TimeField(default=datetime.time(16, 00))
    wednesday_to = models.TimeField(default=datetime.time(16, 00))
    thursday_from = models.TimeField(default=datetime.time(16, 00))
    thursday_to = models.TimeField(default=datetime.time(16, 00))
    friday_from = models.TimeField(default=datetime.time(16, 00))
    friday_to = models.TimeField(default=datetime.time(16, 00))
    saturday_from = models.TimeField(default=datetime.time(16, 00))
    saturday_to = models.TimeField(default=datetime.time(16, 00))
    sunday_from = models.TimeField(default=datetime.time(16, 00))
    sunday_to = models.TimeField(default=datetime.time(16, 00))
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.profile.name)


def DoctorProfileUpdatedAddedToUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    user.email = profile.email
    user.save()
post_save.connect(DoctorProfileUpdatedAddedToUser, sender=Profile,
                  dispatch_uid="create_DocUser_instance")