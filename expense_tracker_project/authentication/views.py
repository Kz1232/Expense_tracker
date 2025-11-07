from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponse
from django.urls import reverse , reverse_lazy
from .forms import LoginForm , SignupForm
from django.contrib.auth import views as authviews
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('myapps:homepage'))
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, "authentication/login.html", context)


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

class pass_reset_view(SuccessMessageMixin , authviews.PasswordResetView):
    template_name = 'authentication/password_reset.html'
    email_template_name = 'authentication/password_reset_email.html'
    subject_template_name = 'authentication/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('myapps:homepage')

class pass_confirm_view(authviews.PasswordResetConfirmView):
    template_name='authentication/password_reset_confirm.html'
    success_url = reverse_lazy('authentication:password_reset_complete')