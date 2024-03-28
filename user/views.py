from django.shortcuts import render, redirect
from user.forms import LoginForms, RegisterForms
from django.contrib.auth.models import User
from django.contrib import messages, auth

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username=form['username'].value()
            password=form['password'].value()

        user = auth.authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{username} successfully logged in')
            return redirect('index')
        else:
            messages.error(request, 'Login Error')
            return redirect('login')

    return render(request, 'user/login.html', {'form':form})

def register(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            if form['password1'].value() != form['password2'].value():
                messages.error(request, 'Password Confirmation Error')
                return redirect('register')
            
            username = form['username_register'].value()
            email = form['email'].value()
            password = form['password1'].value()

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Existing user')
                form.add_error('username_register', "Username already exists")
                return redirect('register')
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, 'Registration completed successfully!')
            return redirect('login')

    return render(request, 'user/register.html', {'form':form})

def logout(request):
    messages.success(request, 'Logout successful!')
    auth.logout(request)
    return redirect('login')
