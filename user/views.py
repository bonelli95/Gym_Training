from django.shortcuts import render, redirect
from user.forms import LoginForms, RegisterForms
from django.contrib.auth.models import User

def login(request):
    form = LoginForms()
    return render(request, 'user/login.html', {'form':form})

def register(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            if form['password1'].value() != form['password2'].value():
                return redirect('register')
            
            username = form['username_register'].value()
            email = form['email'].value()
            password = form['password1'].value()

            if User.objects.filter(username=username).exists():
                form.add_error('username_register', "Username already exists")
                return redirect('register')
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            return redirect('login')

    return render(request, 'user/register.html', {'form':form})