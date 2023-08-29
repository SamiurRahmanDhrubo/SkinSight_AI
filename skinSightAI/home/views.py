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