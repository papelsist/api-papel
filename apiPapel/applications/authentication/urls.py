from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
     path('api/login/', views.login),
     path('api/change-password/', views.changePassword),
]

