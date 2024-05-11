from pickle import TRUE
from turtle import title
from django.db import models
from django.contrib.auth.models import User


# Create your models here
class emp(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
       return self.username
    
class Project(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    task_title = models.CharField(max_length=100, null=True)
    task_description = models.TextField(null=True)
    task_deadline = models.DateField(null=True)
    task_status = models.BooleanField(default=False)

    

    def __str__(self):
        return self.name