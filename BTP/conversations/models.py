from django.db import models
# user used by django for authetication and login in admin page
from django.contrib.auth.models import User
# check django user model for more information
# Create your models here.
# from .doctors import models
from doctors.models import Profile
from clients.models import ClientProfile

import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class MessageData(models.Model):
    senderProfile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="SenderInConversation")
    recieverProfile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="RecieverInConversation")

    messageID = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    messageBody = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    messageImage = models.ImageField(
        null=True, blank=True)
    isRead = models.BooleanField(default=False, null = True)
    
    def __str__(self):
        return self.senderProfile.username + ', ' + self.recieverProfile.username

    class Meta:
        ordering = ['isRead', '-created']    


class Appointment(models.Model):
    senderProfile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="SenderInConversation")
    recieverProfile = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name="RecieverInConversation")

    appointmentID = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False)

    date = models.DateField()
    time = models.TimeField()
    appointmentLink = models.TextField()
    # appointmentPassword = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.senderProfile.username + ', ' + self.recieverProfile.username

    

