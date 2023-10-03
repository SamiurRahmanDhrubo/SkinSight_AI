from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth import logout
from .models import UserProfile, UploadedImage
from .forms import UploadImageForm
from .models import UploadedImage
from .image_classifier import preprocess_and_predict  # Import the preprocess_and_predict function



def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')
   

def features(request):
    return render(request, 'features.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def login_v(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                error_message = "Invalid username or password."
        else:
            error_message = ""

        return render(request, 'login.html', {'error_message': error_message})
    else:
        return redirect('/')
# accounts/views.py


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            full_name = request.POST.get('full_name')
            username = request.POST.get('username')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if not all([full_name, username, phone_number, email, password, confirm_password]):
                messages.error(request, "All fields are required.")
                return render(request, 'register.html')

            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return render(request, 'register.html')

            # Check if a user with the same username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already in use.")
                return render(request, 'register.html')

            # Check if a user with the same email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already in use.")
                return render(request, 'register.html')

            # Create a new user with a unique username and email
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = full_name
            user.save()

            # Create and save user profile
            user_profile = UserProfile(user=user, full_name=full_name, phone_number=phone_number)
            user_profile.save()

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


from .image_classifier import preprocess_and_predict  # Import the preprocess_and_predict function

from .models import UploadedImage

def scan_page(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image to the database
            image_instance = form.save()

            # Use preprocess_and_predict to get the prediction
            prediction = preprocess_and_predict(image_instance.image)

            return render(request, 'result.html', {'image_instance': image_instance, 'prediction': prediction})
    else:
        form = UploadImageForm()

    return render(request, 'scan.html', {'form': form})





    

def result_view(request):
        return render(request, 'result.html')



def profile(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'profile_page.html', {'user_profile': user_profile})
    else:
        return redirect('/login')