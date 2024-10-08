from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)

class Teacher(models.Model):
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250, null=True)

class Course(models.Model):
        title = models.CharField(max_length=250)
        description = models.TextField(null=True, blank=True)
        teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
        students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
                return self.title
