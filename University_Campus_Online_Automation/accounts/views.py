from email.mime import message
from mailbox import Message
from pyexpat.errors import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            username = form.cleaned_data.get('username')
           
            return redirect('Student:student_details')
        else:
             return render(request, 'accounts/signup.html', { 'form': form })
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})