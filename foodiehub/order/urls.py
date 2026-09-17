from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    path('my-cart/', views.cart_view, name='cart'),
    path('checkout', views.checkout_view, name='checkout'),
    path('status/<int:order_id>/', views.order_status_view, name='order_status'),
    path('my-order/', views.order_history_view, name='order_history'),
    path('history/', views.order_history, name='order_history'),
]