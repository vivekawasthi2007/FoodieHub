from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem, OrderMaster
from menu.models import FoodItem
from django.utils import timezone
from datetime import timedelta
from accounts.models import UserProfile

@login_required(login_url='login')
def add_to_cart(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    cart_item = CartItem.objects.filter(user=request.user, food_item=food_item).first()
    
    if cart_item:
        cart_item.delete()
    else:
        CartItem.objects.create(user=request.user, food_item=food_item, quantity=1)
        
    return redirect('menu')

from django.core.mail import send_mail
from .models import Coupon

@login_required(login_url='login')
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect('menu')
        
    total_amount = sum(item.total_price() for item in cart_items)
    
    discount = request.session.get('discount', 0)
    final_amount = max(0, total_amount - discount)
    
    try:
        user_address = request.user.profile.address or "Address not updated"
    except:
        user_address = "Address not updated"
    
    order = OrderMaster.objects.create(
        user=request.user, total_amount=final_amount,
        delivery_address=user_address, status='Preparing'
    )
    
    subject = 'FoodieHub: Order Confirmed!'
    message = f'Hi {request.user.username},\n\nYour order #{order.id} is confirmed!\nTotal Paid: ₹{final_amount}\nIt will be delivered in 30 minutes to: {user_address}.\n\nEnjoy your meal!'
    try:
        send_mail(subject, message, 'your_real_email@gmail.com', [request.user.email])
    except:
        pass 
    
    cart_items.delete()
    request.session['discount'] = 0 
    return redirect('order_status', order_id=order.id)

@login_required(login_url='login')
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.total_price() for item in cart_items)
    discount = 0

    if request.method == 'POST':
        code = request.POST.get('coupon_code')
        coupon = Coupon.objects.filter(code=code, is_active=True).first()
        if coupon:
            discount = coupon.discount_amount
            request.session['discount'] = discount

    final_amount = max(0, total_amount - discount)
    return render(request, 'order/cart.html', {
        'cart_items': cart_items, 'total_amount': total_amount, 
        'discount': discount, 'final_amount': final_amount
    })



@login_required(login_url='login')
def order_status_view(request, order_id):
    order = get_object_or_404(OrderMaster, id=order_id, user=request.user)
    return render(request, 'order/order_status.html', {'order': order})
@login_required(login_url='login')

def order_history_view(request):
    orders = OrderMaster.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order/order_history.html', {'orders': orders})
@login_required(login_url='login')
def order_history(request):
    orders = OrderMaster.objects.filter(user=request.user).order_by('-id')
    return render(request, 'order/order_history.html', {'orders': orders})