from django.shortcuts import render, HttpResponse
from .models import Student
# Create your views here.


def students(request):
    if  request.method == 'GET':
        all_students = Student.objects.all()

        students_list  = [student.name + '\n' for student in all_students]

        return HttpResponse(students_list)

def teachers(request):  # New view for Teacher model
        if request.method == 'GET':
                    all_teachers = Teacher.objects.all()
                    teachers_list = [teacher.name + ' - ' + teacher.subject + '\n' for teacher in all_teachers]
                    return HttpResponse(teachers_list)
            
# View for listing all courses
def courses(request):
    if request.method == 'GET':
        all_courses = Course.objects.all()
        courses_list = [
            f"Course Title: {course.title}, Teacher: {course.teacher.name}, Description: {course.description}\n" 
            for course in all_courses
        ]
        return HttpResponse(''.join(courses_list), content_type='text/plain')
