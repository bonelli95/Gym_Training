from django import forms

class LoginForms(forms.Form):
    name_login = forms.CharField(
        label="Username",
        required=True,
        max_length=20
    )
    password = forms.CharField(
        label="Password",
        required=True,
        max_length=20,
        widget=forms.PasswordInput
    )