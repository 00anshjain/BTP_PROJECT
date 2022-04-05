
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.core.mail import send_mail
from django.conf import settings
from .models import Profile

def DoctorProfileUpdatedAddedToUser(sender, instance, created, **kwargs):
    profile = instance
    # user = profile.user
    # user.email = profile.email
    # user.save()

    if created :
        subject = 'Welcome to DocitMed'
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

post_save.connect(DoctorProfileUpdatedAddedToUser, sender=Profile,
                  dispatch_uid="create_DocUser_instance")