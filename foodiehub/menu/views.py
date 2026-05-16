from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FoodItem, WishlistItem

def menu_page(request):
    query = request.GET.get('q')
    if query:
        foods = FoodItem.objects.filter(name__icontains=query, is_available=True)
    else:
        foods = FoodItem.objects.filter(is_available=True)
        
    # यूज़र के फेवरेट आइटम्स की लिस्ट निकालना (ताकि लाल दिल दिखा सकें)
    user_wishlist = []
    if request.user.is_authenticated:
        user_wishlist = WishlistItem.objects.filter(user=request.user).values_list('food_item_id', flat=True)

    return render(request, 'menu/index.html', {'foods': foods, 'user_wishlist': user_wishlist})
# 1. लाइक/अनलाइक करने का फंक्शन
@login_required(login_url='login')
def toggle_wishlist(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)
    # चेक करें कि क्या यह पहले से फेवरेट है
    wishlist_item = WishlistItem.objects.filter(user=request.user, food_item=food).first()
    
    if wishlist_item:
        wishlist_item.delete()  # अगर है, तो अनलाइक (हटा) दें
    else:
        WishlistItem.objects.create(user=request.user, food_item=food) # नहीं है, तो लाइक (ऐड) कर दें
        
    return redirect('menu')

# 2. फेवरेट पेज दिखाने का फंक्शन
@login_required(login_url='login')
def wishlist_page(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'menu/wishlist.html', {'wishlist_items': wishlist_items})