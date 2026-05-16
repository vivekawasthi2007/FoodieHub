from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# 1. नया अकाउंट बनाने के लिए (Register)
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # अकाउंट बनने के बाद लॉगिन पेज पर भेजें
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# 2. लॉगिन करने के लिए (Login)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu')  # लॉगिन के बाद सीधे मेन्यू पेज पर भेजें
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# 3. लॉगआउट करने के लिए (Logout)
def logout_view(request):
    logout(request)
    return redirect('menu')

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required(login_url='login')
def profile_view(request):
    # चेक करें कि क्या यूज़र की प्रोफाइल पहले से बनी है, नहीं तो नई बना दें
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        # फॉर्म से डेटा उठाना
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        # डेटाबेस में अपडेट करना
        profile.phone_number = phone
        profile.address = address
        profile.save()
        
        return redirect('profile') # वापस प्रोफाइल पेज पर भेजें
        
    return render(request, 'accounts/profile.html', {'profile': profile})