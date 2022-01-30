from django.contrib import admin
from django.urls import path
from . import views
app_name='Student'
urlpatterns = [
    path('',views.student_details,name='student_details'),
]
