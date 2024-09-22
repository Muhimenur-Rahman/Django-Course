from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    dic = {'author' : 'Rayhan',
           'age' : 5,
           'list' : ['Rayhan', 'Rahman', 'Muhimenur'],
           'courses' : [{'id' : 1,'name' : 'python'},
                        {'id' : 2,'name' : 'django'},
                        {'id' : 3,'name' : 'html'},
                        ],
            'birthday' : datetime.datetime.now()
           }
    return render(request,"first_app/home.html",dic)


