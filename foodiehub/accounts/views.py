from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


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


from django.contrib.auth.decorators import login_required
from .models import UserProfile

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