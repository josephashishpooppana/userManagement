from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm  # Built-in login form

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # Populate form with user input
        if form.is_valid():  # Check if form input is valid
            user = form.save()  # Save user to the database
            login(request, user)  # Log in the new user
            return redirect('home')  # Redirect to home page after login
    else:
        form = RegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Use Django's built-in login form
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)  # Authenticate user
            if user is not None:
                login(request, user)  # Log in the user
                messages.success(request, "Login successful!")
                return redirect('home')  # Redirect to home page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})  # Render login page


def user_logout(request):
    logout(request)  # Log out the current user
    return redirect('home')  # Redirect to home page after logout

