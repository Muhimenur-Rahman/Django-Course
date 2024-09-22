
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("form/",views.form,name="form"),
    path("django_form/",views.django_form,name="django_form"),
    path("django_form_2/",views.django_form_2,name="django_form_2"),
    path("django_form_3/",views.django_form_3,name="django_form_3"),
    path("password_validation/",views.password_validation,name="password_validation"),
    path("about/",views.about,name="about"),
]
