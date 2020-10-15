from django.urls import path
from . import views

app_name='login'

urlpatterns=[
        path('',views.login, name='login'),
        path('login', views.login_click, name='login_click'),
        path('signup', views.signup, name='signup'),
        ]
