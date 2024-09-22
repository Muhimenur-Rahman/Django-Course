from django.http import HttpResponse 

def Home(response):
    return HttpResponse("This is a home page")

def contact(request):
    return HttpResponse("This is a contact page")