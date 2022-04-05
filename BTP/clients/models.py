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
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.


class ClientProfile(models.Model):
    GenderChoices = (
        ("M", "Male"),
        ("F", "Female"),
    )
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null = True, blank = True)
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    # ANytime user is deleted the profile is deleted
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GenderChoices, blank=False, null=False)
    dob = models.DateField()
    # age = models.IntegerField(null=False)
    # available_time = models.OneToOneField(
    # 'Availability', on_delete=models.CASCADE, null=True, blank=True)
    # qualifications = models.ManyToManyField('Qualification', blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    # short_intro = models.CharField(max_length=200, blank=True, null=True)
    # bio = models.TextField(blank=True, null=True)
    # is_active = models.BooleanField(default=False)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    # speciality = models.CharField(max_length=200, blank=True, null=True)
    contact_number = PhoneField(blank=True, help_text='Contact phone number')
    # joining_date = models.DateField(auto_now_add=True)
    Cid = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

