from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('api/report/', views.report ),
]

