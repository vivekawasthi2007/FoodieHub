from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FoodItem, WishlistItem, SpecialOffer
from order.models import CartItem  

@login_required(login_url='login')
def menu_page(request):
    query = request.GET.get('q')
    if query:
        foods = FoodItem.objects.filter(name__icontains=query, is_available=True)
    else:
        foods = FoodItem.objects.filter(is_available=True)
        
    user_wishlist = []
    cart_item_ids = []
    offers = SpecialOffer.objects.filter(is_active=True)
    
    if request.user.is_authenticated:
        user_wishlist = WishlistItem.objects.filter(user=request.user).values_list('food_item_id', flat=True)
        cart_item_ids = CartItem.objects.filter(user=request.user).values_list('food_item_id', flat=True)

    return render(request, 'menu/index.html', {
        'foods': foods, 
        'user_wishlist': user_wishlist,
        'cart_item_ids': cart_item_ids,
        'offers': offers
    })

@login_required(login_url='login')
def toggle_wishlist(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)
  
    wishlist_item = WishlistItem.objects.filter(user=request.user, food_item=food).first()
    
    if wishlist_item:
        wishlist_item.delete()  
    else:
        WishlistItem.objects.create(user=request.user, food_item=food) 
        
    return redirect('menu')

@login_required(login_url='login')
def wishlist_page(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'menu/wishlist.html', {'wishlist_items': wishlist_items})