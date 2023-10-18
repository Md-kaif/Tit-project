from django.contrib import admin
from django.urls import path
from tit import views

urlpatterns = [
    path('', views.index, name="home"),
    path('register/', views.register, name="register"),
    path('login', views.loginuser, name="loginuser"),
    path('logout/', views.logout_user, name='logout')
]