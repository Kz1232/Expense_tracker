from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from django.http import HttpResponse
from django.urls import reverse
from .forms import UserForm


# Create your views here.
def login_view(request):
    form = UserForm()
    if request.method == 'POST':
        email = request.POST['email']
        password =request.POST['password']
        user = authenticate(request,email = email , password = password) 
        if user is not None:
            login(request,user)
            return redirect(reverse('myapps:homepage'))



    context={'form':form}
    return render(request ,"authentication/login.html",context)