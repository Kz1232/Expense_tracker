from .models import User
from django import forms 


class LoginForm(forms.ModelForm): 
    class Meta:
        model = User
        fields=['email','password','is_active']

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password']
    
    def clean(self):
        cleaned_data = super().clean()
        
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # This hashes the password
        if commit:
            user.save()
        return user             

