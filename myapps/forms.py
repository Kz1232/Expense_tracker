from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63 ,widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.User
        fields =('username','email','first_name','last_name')
    