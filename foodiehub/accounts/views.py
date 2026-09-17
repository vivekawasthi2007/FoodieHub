from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile
import random

def send_otp_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = str(random.randint(100000, 999999))
        
        request.session['otp'] = otp
        request.session['user_email'] = email
        
        subject = 'FoodieHub: Your OTP Code'
        message = f'Your One Time Password (OTP) for FoodieHub is: {otp}\nDo not share this with anyone.'
        
        # यहाँ हमने 'settings.EMAIL_HOST_USER' लगा दिया है 
        # ताकि यह अपने आप आपकी सेटिंग्स फाइल से आपका असली ईमेल ले ले
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
        
        return redirect('verify_otp')
        
    return render(request, 'accounts/send_otp.html')


def verify_otp_view(request):
    if request.method == 'POST':
        user_entered_otp = request.POST.get('otp')
        real_otp = request.session.get('otp')
        
        if user_entered_otp == real_otp:
            return redirect('menu')
        else:
            return render(request, 'accounts/verify_otp.html', {'error': 'Invalid OTP!'})
            
    return render(request, 'accounts/verify_otp.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu')  
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('menu')


@login_required(login_url='login')
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        profile.phone_number = phone
        profile.address = address
        profile.save()
        
        return redirect('profile') 
        
    return render(request, 'accounts/profile.html', {'profile': profile})