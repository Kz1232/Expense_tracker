from django.urls import path
from . import views
app_name = "myapps"
urlpatterns = [
    path("",views.indexView,name="home"),
    path("accounts/login/",views.login_page,name="loginpage"),
    path("logout/",views.logoutView,name="logout"),
]