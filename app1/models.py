from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)
    
class Teacher(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)