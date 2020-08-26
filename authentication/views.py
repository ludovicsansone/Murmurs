from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.urls import reverse


def registerView(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = User()
        user.username = form.cleaned_data['username']
        user.email = form.cleaned_data['email']
        user.set_password(raw_password = form.cleaned_data['password'])
        user.save()
        envoi = True
        return redirect(reverse('authentication_login'))        
        
    return render(request, 'authentication_register.html', locals())

def loginView(request):
    error = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password) 
            if user:
                login(request, user)
                return redirect('/')
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'authentication_login.html', locals())

def forgetView(request):
    return render(request, 'authentication_forget.html')

def logoutView(request):
    logout(request)
    return redirect('/')
    