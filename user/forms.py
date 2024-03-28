from typing import Any
from django import forms
from django.forms import ModelForm, TextInput, PasswordInput

class LoginForms(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-group",
                "placeholder": "Enter Your Name"
            }
        )
    )
    password = forms.CharField(
        label="Password",
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-group",
                "placeholder": "Enter Your Password"
            }
        )
    )

class RegisterForms(forms.Form):
    username_register = forms.CharField(
        label="Username",
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-group",
                "placeholder": "Your Name"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=30,
        widget=forms.EmailInput(
            attrs={
                "class": "form-group",
                "placeholder": "name@example.com"
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-group",
                "placeholder": "Enter Your Password"
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-group",
                "placeholder": "Confirm Your Password"
            }
        )
    )

    def clean_username_register(self):
        username = self.cleaned_data.get('username_register')

        if username:
            username = username.strip()
            if ' ' in username:
                raise forms.ValidationError('Sorry, it is not possible to include spaces in registration names. Please remove spaces and try again')
            else:
                return username
            
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Password Confirmation Error')
            else:
                return password2
