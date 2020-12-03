from django.db import models
from institute.models import JobCreation
# Create your models here.

class PersonalProfile(models.Model):
    user=models.CharField(max_length=150)
    age=models.IntegerField()
    phonenumber=models.IntegerField(max_length=12,unique=True)
    jobtitle=models.ForeignKey(JobCreation,on_delete=models.CASCADE)
    qualification=models.CharField(max_length=150)
    skills=models.CharField(max_length=500)
    experience=models.IntegerField()
    choices = (
        ('applied','applied'), ('rejected','rejected'), ('accepted','accepted')
    )
    status = models.CharField(max_length=120, choices=choices, default="applied")


    def __str__(self):
        return self.user
class TrainerBidding(models.Model):
    user=models.CharField(max_length=150)
    jobtitle=models.CharField(max_length=150)
    expectedamount=models.IntegerField(max_length=150)

    def __str__(self):
        return self.user

