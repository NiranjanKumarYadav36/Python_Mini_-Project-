# Generated by Django 5.0.2 on 2024-03-18 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_jobseeker_password_recruiter_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='password',
        ),
        migrations.RemoveField(
            model_name='recruiter',
            name='password',
        ),
    ]
