from django.shortcuts import render
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from . import forms

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
            else:
                message = "Login failed"
    return render(request,'authentication/login.html',context={"form":form,"message":message})


