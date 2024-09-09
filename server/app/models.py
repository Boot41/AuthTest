from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Job(models.Model):
    employer = models.ForeignKey(Employer, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=50, choices=[('submitted', 'Submitted'), ('shortlisted', 'Shortlisted'), ('rejected', 'Rejected')], default='submitted')
    applied_at = models.DateTimeField(auto_now_add=True)
