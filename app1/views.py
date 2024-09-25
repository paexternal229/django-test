from django.shortcuts import render, HttpResponse
from .models import Student
# Create your views here.


def students(request):
    if  request.method == 'GET':
        all_students = Student.objects.all()

        students_list  = [student.name + '\n' for student in all_students]

        return HttpResponse(students_list)

