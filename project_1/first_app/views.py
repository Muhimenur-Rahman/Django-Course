from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(response):
    return HttpResponse("This is a first_app Home page")

def courses(response):
    return HttpResponse("This is a first_app course page")


def about(response):
    return HttpResponse("This is a first_app about page")