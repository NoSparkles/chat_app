from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from . import models

def index(request):
    return render(request, 'base/index.html', {})

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = get_user_model()
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'base/register.html', {})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username ,password)
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print('logged')
                login(request, user)
                return redirect('index')
        
    return render(request, 'base/login.html', {})


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')

def chat_page(request):
    if not request.user.is_authenticated:
        return redirect('index')
    
    username = request.user.username

    return render(request, 'base/chat.html', {'username': username})