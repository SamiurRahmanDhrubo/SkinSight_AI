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
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.landing, name='landing'),
    path('faq/', home.views.faq, name='faq_page'),
    path('faq2/', home.views.faq2, name='faq_page2'),
    path('home/', home.views.home, name='home_page'),
    path('Payment/', home.views.paypop, name='popUp'),

    path('admin_page/', home.views.admin_page, name='admin_page'),
    path('toggle_payment_status/<int:request_id>/', home.views.toggle_payment_status, name='toggle_payment_status'),
    path('payment/', home.views.payment, name='payment_page'),
    path('terms/', home.views.term, name='t&c_page'),
    path('terms2/', home.views.term2, name='t&c_page2'),

    path('login/', home.views.login_v, name='login_page'),
    path('feature/', home.views.features, name='feature_page'),
    path('feature2/', home.views.features2, name='feature_page2'),

    path('register/', home.views.register, name='register_page'),
    path('contact/', home.views.contact, name='contact'),
    path('contact2/', home.views.contact2, name='contact2'),

    path('about/', home.views.about, name='about'),
    path('about2/', home.views.about2, name='about2'),
    path('ai/', home.views.ai, name='artificial_intelligence'),
    path('ai2/', home.views.ai2, name='artificial_intelligence2'),
    path('history/', home.views.history, name='history'),
    path('profile/', home.views.profile, name='profile_page'),
    path('logout/', home.views.logout_view, name='logout'),
    path('scan/', home.views.scan_page, name='scan_page'),\
    path('check_payment_status/', home.views.check_payment_status, name='check_payment_status'),
    path('result/', home.views.result_view, name='result_page'),
    path('resulthistory/', home.views.result_history, name='result_history'),
    path('password_reset/',auth_views.PasswordResetView.as_view(
        template_name = 'password_reset.html'
    ),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(
        template_name = 'password_reset_done.html'
    ),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(
        template_name = 'password_reset_confirm.html'
    ),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(
        template_name = 'password_reset_complete.html'
    ),name='password_reset_complete'),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
