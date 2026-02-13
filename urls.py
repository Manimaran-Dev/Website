from django.urls import path
from . import views

urlpatterns = [
    path("Sign/",views.Signup,name="NewAccount"),
    path("Login/",views.LoginPage,name="loginPage"),
    path("Home/",views.HomePage,name="HomePage"),
]