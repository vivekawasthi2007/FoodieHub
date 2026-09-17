import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodiehub.settings')
django.setup()

from menu.models import SpecialOffer

def run_seed():
    SpecialOffer.objects.all().delete()
    
    offers_list = [
        {"title": "50% Off Pizza", "price": 299, "description": "Get flat 50% discount on all large Italian pizzas today!", "image_url": "https://images.unsplash.com/photo-1513104890138-7c749659a591"},
        {"title": "Burger Combo", "price": 199, "description": "Buy 1 Double Cheese Burger and get French Fries free.", "image_url": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"},
        {"title": "Sweet Sunday", "price": 149, "description": "Special chocolate brownie with vanilla ice cream at ₹149 only.", "image_url": "https://images.unsplash.com/photo-1563805042-7684c019e1cb"},
        {"title": "Weekend Dhamaka", "price": 349, "description": "Flat ₹150 off on total cart value using code WEEKEND.", "image_url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5"},
        {"title": "Cold Coffee Treat", "price": 120, "description": "Creamy thick cold coffee with extra chocolate syrup at 30% off.", "image_url": "https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5"},
        {"title": "Spicy Momos Deal", "price": 110, "description": "Get 2 plates of Veg/Paneer Steam Momos at the price of 1!", "image_url": "https://images.unsplash.com/photo-1626777552726-4a6b54c97e46"},
        {"title": "Pasta Paradise", "price": 249, "description": "White sauce creamy pasta loaded with cheese and olives.", "image_url": "https://images.unsplash.com/photo-1621996346565-e3d5d628359b"},
        {"title": "French Fries Fest", "price": 99, "description": "Peri-peri masala fries with cheesy dip starting at just ₹99.", "image_url": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877"},
        {"title": "Healthy Sandwich", "price": 159, "description": "Grilled corn and cheese sandwich with fresh mint mojito.", "image_url": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af"},
        {"title": "South Indian Feast", "price": 179, "description": "Crispy butter masala dosa with extra sambhar and coconut chutney.", "image_url": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976"},
        {"title": "North Indian Thali", "price": 299, "description": "Complete dinner thali with paneer lababdar, dal makhani, and butter naan.", "image_url": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc"},
        {"title": "Pani Puri Treat", "price": 79, "description": "Hygenic and spicy 6-flavoured pani puri plate free with orders above ₹600.", "image_url": "https://images.unsplash.com/photo-1601050690597-df0568f70950"},
        {"title": "Chocolate Shake", "price": 139, "description": "Oreo heavy chocolate milkshake topped with whipped cream.", "image_url": "https://images.unsplash.com/photo-1572490122747-3968b75cc699"},
        {"title": "Spring Rolls Special", "price": 189, "description": "Crispy crunchy vegetable spring rolls served with spicy schezwan sauce.", "image_url": "https://images.unsplash.com/photo-1548365328-8b2226b362b3"},
        {"title": "Midnight Cravings", "price": 279, "description": "Late night special combo: Veg Noodles + Manchurian at flat 40% off.", "image_url": "https://images.unsplash.com/photo-1585032226651-759b368d7246"}
    ]

    for offer_data in offers_list:
        SpecialOffer.objects.create(
            title=offer_data["title"],
            price=offer_data["price"],
            description=offer_data["description"],
            image_url=offer_data["image_url"],
            is_active=True
        )
    
    print("✨ All 15 Special Offers with Correct Prices Added Successfully! ✨")

if __name__ == '__main__':
    run_seed()