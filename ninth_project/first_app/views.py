from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.

def home(request):
    respone = render(request,'home.html')
    respone.set_cookie('name','Rayhan',expires=datetime.now() + timedelta(days=7))
    return respone

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'cookie.html',{'name' : name})


def delete_cookie(request):
    respone = render(request,'delete.html')
    respone.delete_cookie('name')
    return respone

def set_session(request):
    # data = {
    #     'name' : 'Rayhan',
    #     'age' : 20,
    #     'language' : 'Bangla',
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name'] = 'rayhan'
    return render(request,'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name','Guest')
        request.session.modified = True
        return render(request,'session.html',{'name' : name})
    else:
        return HttpResponse('Your Sesssion Has Been Expired. Log in again')

def delete_session(request):
    request.session.flush()
    # *** del request.session['name'] *** this is an alternative
    return render(request,'delete.html')
