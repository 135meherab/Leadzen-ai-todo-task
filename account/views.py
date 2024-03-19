from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            print(user_name, user_password)
            user = authenticate(username = user_name, password =user_password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home_page')
