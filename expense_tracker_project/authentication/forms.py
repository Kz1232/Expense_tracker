from .models import User
from django import forms
from django.core.exceptions import ValidationError 
from django.contrib.auth.password_validation import validate_password


class LoginForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password']

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password :
            raise ValidationError('Password are not matching')
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.instance.pk is None:  # Only check for new users
            if User.objects.filter(email=email).exists():
                raise ValidationError("User with email already exists !!!")
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            validate_password(password)
        return password
    

    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # This hashes the password
        if commit:
            user.save()
        return user             

