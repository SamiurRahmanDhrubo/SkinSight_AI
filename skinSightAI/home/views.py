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
from .models import PaymentRequest
from django.http import JsonResponse
from .forms import UserProfileForm


def check_payment_status(request):
    if request.user.is_authenticated:
        user_phone_number = request.user.userprofile.phone_number
        payment_request = PaymentRequest.objects.filter(phone_number=user_phone_number).first()
        if payment_request and payment_request.payment_status == 1:
            return JsonResponse({'payment_status': 1})
    
    return JsonResponse({'payment_status': 0})
def toggle_payment_status(request, request_id):
    try:
        payment_request = PaymentRequest.objects.get(id=request_id)
        
        # Toggle the payment status of PaymentRequest
        payment_request.payment_status = not payment_request.payment_status
        payment_request.save()
        
        # Retrieve the associated UserProfile
        user_profile = UserProfile.objects.get(full_name=payment_request.full_name)
        
        # Toggle the payment status of UserProfile
        user_profile.payment_status = payment_request.payment_status
        if user_profile.payment_status == 1:
            user_profile.value = 5
        else:
            user_profile.value = 0
        user_profile.save()
        
        return JsonResponse({'status': 'done' if payment_request.payment_status else 'pending'})
    except PaymentRequest.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

def landing(request):
    return render(request, 'landing.html')
def admin_page(request):
    # Retrieve all PaymentRequest records
    payment_requests = PaymentRequest.objects.all()
    
    return render(request, 'admin.html', {'payment_requests': payment_requests})

    
    return render(request, 'admin.html', {'payment_requests': payment_requests})

def home(request):
    return render(request, 'home.html')
def check_payment_status(request):
    if request.user.is_authenticated:
        user_phone_number = request.user.userprofile.phone_number
        payment_request = PaymentRequest.objects.filter(phone_number=user_phone_number).first()
        if payment_request and payment_request.payment_status == 1:
            return JsonResponse({'payment_status': 1})
      

def features(request):
    return render(request, 'features.html')



def history(request):
    if request.user.is_authenticated:
        # Get the user's phone number
        user_phone_number = request.user.userprofile.phone_number  # Replace 'userprofile' with your user's profile model if needed

        # Query the PaymentRequest table for records with the matching phone number
        payment_requests = PaymentRequest.objects.filter(phone_number=user_phone_number)

        return render(request, 'history.html', {'payment_requests': payment_requests})
    else:
        return redirect('/login')

def logout_view(request):
    logout(request)
    return redirect('/')

def login_v(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            
            # Check if it's an admin login
            if username == 'Admin' and password == 'Admin':
                user = User.objects.get(username='Admin')
                login(request, user)
                return redirect('admin_page')  # Redirect to the admin page
            else:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home_page')  # Redirect to the home page for regular users
                else:
                    error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
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
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.payment_status and user_profile.value > 0:
            if request.method == 'POST':
                form = UploadImageForm(request.POST, request.FILES)
                if form.is_valid():
                    # Save the uploaded image to the database
                    image_instance = form.save()

                    # Use preprocess_and_predict to get the prediction
                    prediction = preprocess_and_predict(image_instance.image)

                    # Deduct one from the available scans
                    user_profile.value -= 1
                    user_profile.save()

                    return render(request, 'result.html', {'image_instance': image_instance, 'prediction': prediction, 'user_profile': user_profile})
            else:
                form = UploadImageForm()
            return render(request, 'scan.html', {'form': form, 'user_profile': user_profile})
        else:
            return redirect('/payment')
    else:
        return redirect('/login')





    

def result_view(request):
        return render(request, 'result.html')

def payment(request):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        
        # Verify payment status with the payment gateway (implementation dependent on the gateway used)
        # If payment is successful, the payment gateway will send a callback/webhook
        
        # Check if the phone number matches the one associated with the user's profile
        if request.POST.get('phone_number') == user_profile.phone_number:
            # Create a new PaymentRequest record
            payment_request = PaymentRequest(
                full_name=request.POST.get('name'),
                phone_number=user_profile.phone_number,
                payment_status=False  # Set to True since payment is successful
            )
            payment_request.save()
            
            # Update the UserProfile based on PaymentRequest's payment status
            
            
            return redirect('/home')  # Redirect to the home page after successful payment and phone number match
        else:
            return render(request, 'payment.html', {'error_message': 'Phone number does not match.'})
    else:
        return render(request, 'payment.html')

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    return render(request, 'profile_page.html', {'user_profile': request.user.userprofile, 'form': form})

# if PaymentRequest.payment_status == True:
            #     user_profile.payment_status = True
            #     user_profile.value = 5
            #     user_profile.save()
            # user_profile.payment_status = True
            # user_profile.value = 5
            # user_profile.save()