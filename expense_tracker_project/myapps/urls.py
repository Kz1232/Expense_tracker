from django.urls import path
from . import views

app_name = 'myapps'
urlpatterns = [
    path('',views.homepage,name="homepage"),
]