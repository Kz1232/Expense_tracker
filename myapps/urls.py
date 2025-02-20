from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
app_name = "myapps"
urlpatterns = [
    path("",views.indexView,name="home"),
    path("login/",views.login_page,name="loginpage"),
    path("logout/",views.logoutView,name="logout"),
    path("signup/",views.signup_page,name="signup"),
]