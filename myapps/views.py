from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from . import forms
import time
# Create your views here.
@login_required
def indexView(request):
    activeUser=request.user
    context={"user":activeUser}
    return render(request ,"myapps/index.html",context)

def login_page(request):
    form = forms.LoginForm()
    message = None
    if request.method == 'POST':
        form =forms.LoginForm(request.POST or None)
        if form.is_valid():
            user =authenticate(
                username=form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                message = f'Hello{user.username}! Logged in successfull'
                time.sleep(5)
                return redirect('/')
            else:
                message = "Login failed"
    return render(request,'authentication/login.html',context={"form":form,"message":message})


def logoutView(request):
    logout(request)
    return redirect('/')
    
    