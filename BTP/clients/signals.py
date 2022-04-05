from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import ClientProfile




def ClientProfileUpdatedAddedToUser(sender, instance, created, **kwargs):
    if created:
        # print(profile)
        # print(profile.email)
        profile = instance
        # user = profile.user
        # user.email = profile.email
        # user.save()
        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

post_save.connect(ClientProfileUpdatedAddedToUser, sender=ClientProfile,
                  dispatch_uid="create_ClientUser_instance")