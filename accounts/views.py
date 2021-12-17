from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Student
from .forms import RegisterForm


# Create your views here.


def register(request):
    context = {"form":RegisterForm}
    return render(request, 'accounts/auth_register.html', context)


def login_student(request):
    page_title = 'Login/Register'
    context = {'page_title': page_title}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # this would have to become a custom user (e.g. student)
        student = authenticate(username=username, password=password)
        if student is not None:
            print(student)
            login(request, student)
            messages.success(request, 'Welcome ')
            return redirect('evaluations')
        else:
            print('login error')
            messages.error(request, 'Login error, credentials invalid')
            return redirect('login_student')
    return render(request,'accounts/auth/login.html', context)


def logout_student(request):
    logout(request)
    return redirect('login_student')