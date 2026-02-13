from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def Signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        conform_password = request.POST["conform_password"]
        email = request.POST["email"]
        if password != conform_password:
            messages.error(request,"Passwords do not match")
            return redirect("NewAccount")
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username Already Exists")
            return redirect("loginPage")
        else:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            messages.success(request,"Account Created Successfully")
            return redirect("loginPage")
    return render(request,"authApp/Signup.html")

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("HomePage")

    return render(request,"authApp/Login.html")

def HomePage(request):
    return render(request,"authApp/Homepage.html")

