from django.shortcuts import render
from django.http import HttpResponse

from .import views
from django.urls import path,include

urlpatterns=[
    
    path("",views.index,name="index"),
    path("base/",views.base,name="login"),
    path("login1/",views.login1,name="login1"),
    path("signup1/",views.Signedup.as_view(),name="login1"),
    path("index/",views.logout,name="logout"),
    path("bmi/",views.bmi,name="BMI"),
    path("bmr/",views.calorie,name="BMR"),
    path("diet/",views.diet,name="diet"),


    
    
    
    ]