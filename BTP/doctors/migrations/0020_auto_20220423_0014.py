# Generated by Django 3.2.8 on 2022-04-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0019_alter_profile_registrationnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='registrationNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='stateMedicalCouncil',
            field=models.TextField(default='', max_length=300),
        ),
    ]