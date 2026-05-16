from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem, OrderMaster
from menu.models import FoodItem
from django.utils import timezone
from datetime import timedelta
from accounts.models import UserProfile

# 1. कार्ट में आइटम डालने का फंक्शन
@login_required(login_url='login')
def add_to_cart(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, food_item=food)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('menu')

# 2. कार्ट देखने का फंक्शन
@login_required(login_url='login')
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.total_price() for item in cart_items)
    
    return render(request, 'order/cart.html', {'cart_items': cart_items, 'total_amount': total_amount})

# 3. आर्डर प्लेस (Checkout) करने का नया फंक्शन
# सबसे ऊपर ये लाइन ज़रूर जोड़ लें (अगर नहीं है तो)


@login_required(login_url='login')
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    if not cart_items:
        return redirect('menu')
        
    total_amount = sum(item.total_price() for item in cart_items)
    
    # यूज़र का असली एड्रेस प्रोफाइल से निकालना
    try:
        user_address = request.user.profile.address
        if not user_address:
            user_address = "Address not updated in profile"
    except:
        user_address = "Address not updated in profile"
    
    # नया आर्डर बनाना (असली एड्रेस के साथ)
    order = OrderMaster.objects.create(
        user=request.user,
        total_amount=total_amount,
        delivery_address=user_address, # यहाँ अब असली एड्रेस जाएगा
        status='Preparing'
    )
    
    cart_items.delete()
    return redirect('order_status', order_id=order.id)

# 4. आर्डर का लाइव स्टेटस (30 Min Timer) देखने का फंक्शन
@login_required(login_url='login')
def order_status_view(request, order_id):
    order = get_object_or_404(OrderMaster, id=order_id, user=request.user)
    return render(request, 'order/order_status.html', {'order': order})
@login_required(login_url='login')

def order_history_view(request):
    orders = OrderMaster.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order/order_history.html', {'orders': orders})