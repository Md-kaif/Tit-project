from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login')
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        # phone = request.POST.get("phone")
        username = request.POST.get("username")
        password1 = request.POST.get("pass1")
        password2 = request.POST.get("pass2")
        if password1 != password2:
            messages.info(request, "Username already exist")
            return redirect('register')
        else:
            user = User.objects.filter(username = username)
            if user.exists():
                messages.info(request, "Username already exist")
                return redirect('register')
            
        user = User.objects.create(
            email=email,
            # phone=phone,
            username=username
        )
        user.set_password(password1)
        user.save()
        
        messages.success(request, "Account created successfully.")
        return redirect('/login')
    return render(request, "registration.html")


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login')
        user = authenticate(request, username = username, password= password)

        if user is None:
            messages.info(request,"Invalid Password")
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/')
        
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect('/login')