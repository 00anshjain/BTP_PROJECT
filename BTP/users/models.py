# from django.db import models

# Create your models here.

# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver

# from django.contrib.auth.models import User
# from doctors.models import Profile



# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.db.models.deletion import CASCADE
# import datetime

# import uuid
# from uuid import uuid4

# def generateUUID():
#     return str(uuid4())

# from django.conf import settings
# session_client = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)




# class User(AbstractUser):
#     GENDERCHOICE = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     age = models.IntegerField(null=False, default = 25)
#     gender = models.CharField(
#         max_length=1,
#         choices=GENDERCHOICE,
#         default = 'M'
#     )
#     Uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
#     isDoctor = models.BooleanField('Is doctor', default=False)
    
# fields = ['first_name', 'last_name', 'email', 'age', 'gender', 'username', 'password1', 'password2']
       











# def createProfile(sender, instance, created, **kwargs):
#     if created:
#         user = instance
#         profile = Profile.objects.create(
#             user=user,
#             email = user.email,
#             name = user.first_name + ' ' + user.last_name,
#             username = user.username,

#             )

# post_save.connect(createProfile, sender=User)



# post_delete.connect(deleteUser, sender=Profile)
