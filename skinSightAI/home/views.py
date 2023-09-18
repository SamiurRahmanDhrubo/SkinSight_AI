from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password


def landing(request):
    return render(request, 'landing.html')

def user_profile(request):
    return render(request, 'profile_page.html')    


def features(request):
    return render(request, 'features.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login(request):
    if not request.user.is_authenticated:  
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Replace 'about' with the URL name of your about page
                return redirect('about')
            else:
                error_message = "Invalid username or password."
        else:
            error_message = ""

        return render(request, 'login.html', {'error_message': error_message})
    else:
        return redirect('/')



def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            full_name = request.POST['full_name']
            username = request.POST['username']
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

            # Check if username is already in use
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already in use.")
                return render(request, 'register.html')

            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.first_name = full_name
            user.save()

            # Add a success message
            messages.success(request, "Registration Successful")

            return redirect('/login')
        return render(request, "register.html")
    else:
        return redirect('/')

def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def ai(request):
    return render(request, 'ai.html')

def faq(request):
    return render(request, 'faq.html')

def term(request):
    return render(request, 'terms.html')
