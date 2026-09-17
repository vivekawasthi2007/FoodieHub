from django.contrib import admin
from .models import FoodItem, WishlistItem, SpecialOffer

admin.site.register(FoodItem)
admin.site.register(WishlistItem)

class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    search_fields = ('title',)

admin.site.register(SpecialOffer, SpecialOfferAdmin)

