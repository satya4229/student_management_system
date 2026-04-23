from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.core.mail import send_mail
from django.conf import settings

# LIST PAGE
def student_list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})


# ADD
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def add_student(request):
    if request.method == "POST":

        student = Student.objects.create(
            student_id=request.POST['student_id'],
            full_name=request.POST['full_name'],
            dob=request.POST.get('dob'),
            gender=request.POST['gender'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            course=request.POST['course'],
            year=request.POST['year'],
            gpa=request.POST['gpa']
        )

        # EMAIL SEND (SAFE VERSION)
        try:
            send_mail(
                'Registration Successful',
                f'Hello {student.full_name}, you are successfully registered!',
                settings.EMAIL_HOST_USER,
                [student.email],
                fail_silently=False,
            )

            messages.success(request, "Student registered successfully & email sent!")
            return redirect('student_list')

        except Exception as e:
            messages.warning(request, "Student saved but email NOT sent!")

        return redirect('student_list')

    return render(request, 'form.html')

def item_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'item_view.html', {'student': student})

# EDIT
def edit_student(request, student_id):
    student = Student.objects.get(student_id=student_id)

    if request.method == 'POST':
        student.full_name = request.POST['full_name']

        dob = request.POST.get('dob')
        if dob:
            student.dob = dob
        else:
            student.dob = None
        student.gender = request.POST['gender']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.address = request.POST['address']
        student.course = request.POST['course']
        student.year = request.POST['year']
        student.gpa = request.POST['gpa']
        student.save()

        return redirect('student_list')

    return render(request, 'edit.html', {'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    student.delete()
    return redirect('student_list')