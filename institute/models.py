from django.db import models

# Create your models here.
class JobCreation(models.Model):
    job_name=models.CharField(max_length=120)

    def __str__(self):
        return self.job_name
class JobRequirements(models.Model):
    job_title=models.ForeignKey(JobCreation,on_delete=models.CASCADE)
    skills=models.CharField(max_length=120)
    qualifications=models.CharField(max_length=120)

    def __str__(self):
        return self.job_title