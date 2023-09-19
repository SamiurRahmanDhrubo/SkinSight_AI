"""skinSightAI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.landing, name='landing'),
    path('faq/', home.views.faq, name='faq_page'),
    path('terms/', home.views.term, name='t&c_page'),
    path('login/', home.views.login_v, name='login_page'),
    path('feature/', home.views.features, name='feature_page'),
    path('register/', home.views.register, name='register_page'),
    path('contact/', home.views.contact, name='contact'),
    path('about/', home.views.about, name='about'),
    path('ai/', home.views.ai, name='artificial_intelligence'),
    path('profile/', home.views.user_profile, name='profile_page'),



]
