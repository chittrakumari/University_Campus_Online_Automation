from django.contrib import admin
from django.urls import path
from . import views
#hello
urlpatterns = [
    path('',views.student_details),
]
