from django.db import models

# Create your models here.


class Recruiter(models.Model):
    full_name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    website = models.CharField(max_length=200, blank=True, null=True)
    past_activity = models.CharField(max_length=200, blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    company_details = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True, default='request pending')
    type = models.CharField(max_length=45, blank=True, null=True, default='recruiter')
    image = models.ImageField(null=True)


class JobSeeker(models.Model):
    full_name = models.CharField(max_length=200)
    email_id = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=10)
    location = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/', max_length=100, blank=True, null=True)
    type = models.CharField(max_length=45, null=True, default='seeker')
    image = models.ImageField(null=True)


class Job(models.Model):
    title = models.CharField(max_length=45)
    salary = models.CharField(max_length=45)
    skills = models.CharField(max_length=45)
    job_type = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    start_date = models.CharField(max_length=45)
    deadline = models.CharField(max_length=45)
    recruiter = models.ForeignKey('Recruiter', models.CASCADE)


class Application(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey('JobSeeker', models.CASCADE)
    job = models.ForeignKey('Job', models.CASCADE)


