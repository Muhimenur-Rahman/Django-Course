from django.shortcuts import render
from . forms import contact_forms,student_forms,another_forms,password_forms

# Create your views here.

def index(request):
    return render(request,"first_app/index.html")

def form(request):
    return render(request,"first_app/form.html")


def about(request):
    if(request.method == "POST"):
        name = request.POST.get("username")
        email = request.POST.get("email")
        return render(request,"first_app/about.html",{'name' : name, 'email' : email})
    else:
        return render(request,"first_app/about.html")
    
def django_form(request):
    if request.method == 'POST':
        form = contact_forms(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
        return render(request,"first_app/django_form.html",{'form' : form})
    else:
        form = contact_forms()
    
    return render(request,"first_app/django_form.html",{'form' : form})


def django_form_2(request):
    if request.method == 'POST':
        form = student_forms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = student_forms()
    return render(request,"first_app/django_form.html",{'form' : form})


def django_form_3(request):
    if request.method == 'POST':
        form = another_forms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = another_forms()
    return render(request,"first_app/django_form.html",{'form' : form})


def password_validation(request):
    if request.method == 'POST':
        form = password_forms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = password_forms()
    return render(request,"first_app/django_form.html",{'form' : form})