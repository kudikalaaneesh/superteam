
from turtle import home
from . import views
from django.urls import path
from django.contrib import admin

urlpatterns =[
                 
             path('vs',views.just),
             path('vsmart',views.home)




]