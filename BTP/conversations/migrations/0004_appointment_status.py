# Generated by Django 4.0.1 on 2022-11-06 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0003_remove_appointment_appointmentpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]