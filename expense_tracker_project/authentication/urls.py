from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'authentication'
urlpatterns =[
    # path('',views.testview,name='testview'),
    path('login/',views.login_view,name="login"),
    path('signup/',views.Signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('password-reset',views.pass_reset_view.as_view(),name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         views.pass_confirm_view.as_view(),name='password_reset_confirm'),
    path('password_reset_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),
         name='password_reset_complete'),
    

]