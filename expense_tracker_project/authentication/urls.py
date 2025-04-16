from django.urls import path
from . import views
app_name = 'authentication'
urlpatterns =[
    # path('',views.testview,name='testview'),
    path('login/',views.login_view,name="login"),
]