from django.shortcuts import render,redirect
from . import models

# Create your views here.

def home(request):
    student = models.student.objects.all()
    print(student)
    return render(request,"first_app/home.html",{'student' : student})


def delete_student(request,roll):
    std = models.student.objects.get(pk = roll).delete()
    return redirect("home")

