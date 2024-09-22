from django.urls import path
from . import views
urlpatterns = [
    path('',views.set_session,name='homepage'),
    path('get/',views.get_session,),
    path('delete/',views.delete_session,),
]