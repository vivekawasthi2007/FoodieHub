from django.contrib import admin
from .models import CartItem, OrderMaster, Coupon

admin.site.register(CartItem)
admin.site.register(OrderMaster)
admin.site.register(Coupon)
# Register your models here.
