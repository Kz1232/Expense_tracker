from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponse
from django.urls import reverse
from .forms import LoginForm , SignupForm


# Create your views here.
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password =request.POST['password']
        user = authenticate(request,email = email , password = password) 
        if user is not None:
            login(request,user)
            return redirect(reverse('myapps:homepage'))



    context={'form':form}
    return render(request ,"authentication/login.html",context)


def Signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authentication:login')

    context={'form':form}
    return render(request,"authentication/Signup.html",context)

def logout_view(request):
    logout(request)
    return redirect(reverse('myapps:homepage'))
