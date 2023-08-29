from django.shortcuts import render, redirect


def landing(request):
        return render(request, 'landing.html')

def login(request):
        return render(request, 'login.html')