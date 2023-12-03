from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

def signup(request):
    error=""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')  # Redirect to home page or any other desired URL
        else:
            error=form.errors
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form,"error":error})

def login(request):
    error=""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')  # Redirect to home page or any other desired URL
        else:
            error=form.errors            
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form,"error":error})
