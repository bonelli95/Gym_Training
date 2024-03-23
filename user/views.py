from django.shortcuts import render
from user.forms import LoginForms

def login(request):
    form = LoginForms()
    return render(request, 'user/login.html', {'form':form})

def register(request):
    return render(request, 'user/register.html')
