from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_page, name='menu'),
    path('wishlist/', views.wishlist_page, name='wishlist'), # फेवरेट पेज
    path('wishlist/toggle/<int:food_id>/', views.toggle_wishlist, name='toggle_wishlist'), # लाइक बटन
]