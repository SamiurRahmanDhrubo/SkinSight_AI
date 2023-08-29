from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def landing(request):
        return render(request, 'landing.html')

def login(request):
       if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            error_message = "Invalid username or password."
       else:
        error_message = ""

       return render(request, 'login.html', {'error_message': error_message})

# accounts/views.py

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        # Check if email is already in use
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return render(request, 'register.html')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = full_name
        user.save()

        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login')  # Replace 'login' with the URL name of your login page

    return render(request, 'register.html')
