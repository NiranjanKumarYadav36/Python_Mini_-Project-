# Generated by Django 5.0.2 on 2024-03-03 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('salary', models.CharField(max_length=45)),
                ('skills', models.CharField(max_length=45)),
                ('job_type', models.CharField(max_length=45)),
                ('location', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('start_date', models.CharField(max_length=45)),
                ('deadline', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email_id', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200, unique=True)),
                ('mobile_no', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=200)),
                ('resume', models.CharField(blank=True, max_length=45, null=True)),
                ('type', models.CharField(default='seeker', max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email_id', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=10)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('past_activity', models.CharField(blank=True, max_length=200, null=True)),
                ('skills', models.CharField(blank=True, max_length=200, null=True)),
                ('company_details', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('type', models.CharField(blank=True, default='recruiter', max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobseeker')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='recruiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.recruiter'),
        ),
    ]
