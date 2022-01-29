from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request,'login.html');

def home_page(request):
    return render(request,'homepage.html');
