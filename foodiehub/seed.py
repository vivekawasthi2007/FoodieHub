import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodiehub.settings')
django.setup()

from menu.models import Category, FoodItem

def seed_data():
    print("🧹 ...")
    FoodItem.objects.all().delete()
    
    print("🚀")

    menu_data = {
        "Starters & Snacks": [
            ("🍟 French Fries", 99), ("🍟 Peri Peri Fries", 129), ("🥔 Potato Wedges", 149), 
            ("🌯 Veg Spring Roll", 149), ("🌯 Chicken Spring Roll", 189), ("🍢 Paneer Tikka", 249), 
            ("🍢 Chicken Tikka", 299), ("🧆 Veg Manchurian Dry", 189), ("🍗 Chilli Chicken Dry", 259), 
            ("🌽 Crispy Corn", 169), ("🥖 Garlic Bread", 129), ("🧀 Cheese Garlic Bread", 159), 
            ("🧆 Hara Bhara Kabab", 199), ("🍢 Paneer Seekh Kabab", 229), ("🥔 Honey Chilli Potato", 179), 
            ("🧅 Crispy Onion Rings", 149), ("🍗 Chicken Wings", 249), ("🍗 Chicken Lollipops", 279), 
            ("🥟 Veg Fried Momos", 129), ("🥟 Chicken Steamed Momos", 149)
        ],
        "Main Course": [
            ("🍲 Dal Makhani", 220), ("🥣 Yellow Dal Tadka", 180), ("🥘 Paneer Butter Masala", 280), 
            ("🥘 Kadai Paneer", 270), ("🍲 Shahi Paneer", 290), ("🥗 Mix Veg Curry", 210), 
            ("🧆 Malai Kofta", 260), ("🍗 Butter Chicken", 350), ("🥘 Chicken Tikka Masala", 340), 
            ("🥚 Egg Curry", 220), ("🍖 Mutton Rogan Josh", 450), ("🍚 Veg Dum Biryani", 250), 
            ("🍗 Chicken Biryani", 320), ("🍖 Mutton Biryani", 390), ("🍚 Jeera Rice", 140), 
            ("🍚 Steamed Rice", 110), ("🫓 Butter Naan", 45), ("🫓 Garlic Naan", 55), 
            ("🫓 Tandoori Roti", 25), ("🫓 Lachha Paratha", 40)
        ],
        "Pizzas & Pastas": [
            ("🍕 Margherita Pizza", 199), ("🍕 Farmhouse Veg Pizza", 299), ("🍕 Veg Supreme Pizza", 349), 
            ("🍕 Paneer Tikka Pizza", 329), ("🍕 Mushroom Delight Pizza", 289), ("🍕 Double Cheese Margherita", 259), 
            ("🍕 BBQ Chicken Pizza", 379), ("🍕 Chicken Pepperoni Pizza", 399), ("🍕 Non-Veg Supreme Pizza", 429), 
            ("🍕 Spicy Chicken Pizza", 369), ("🍝 Penne Arrabiata (Red)", 229), ("🍝 Alfredo Pasta (White)", 249), 
            ("🍝 Mix Sauce Pasta (Pink)", 259), ("🧀 Mac and Cheese", 279), ("🍝 Spaghetti Bolognese", 349), 
            ("🍝 Chicken Alfredo Pasta", 299), ("🍝 Baked Veg Pasta", 269), ("🍝 Pesto Pasta", 289), 
            ("🍕 Four Cheese Pizza", 359), ("🍕 Jalapeno & Corn Pizza", 249)
        ],
        "Desserts": [
            ("🍫 Chocolate Brownie", 120), ("🍨 Brownie with Ice Cream", 160), ("🧆 Gulab Jamun (2 pcs)", 80), 
            ("🥣 Rasmalai (2 pcs)", 100), ("🍦 Vanilla Ice Cream", 70), ("🍨 Chocolate Ice Cream", 90), 
            ("🍧 Strawberry Ice Cream", 80), ("🍨 Butterscotch Ice Cream", 90), ("🍰 Red Velvet Cake (Slice)", 180), 
            ("🍰 Black Forest (Slice)", 150), ("🍰 Cheesecake (Slice)", 220), ("🧁 Choco Lava Cake", 130), 
            ("🍮 Tiramisu", 250), ("🍮 Moong Dal Halwa", 140), ("🍮 Gajar Ka Halwa", 150), 
            ("🥗 Fruit Salad with Cream", 160), ("🍮 Chocolate Mousse", 180), ("🧇 Nutella Waffles", 220), 
            ("🥞 Maple Syrup Pancakes", 190), ("🍧 Mango Sorbet", 120)
        ],
        "Beverages": [
            ("💧 Mineral Water (1L)", 40), ("🥤 Coca Cola (330ml)", 60), ("🥤 Sprite (330ml)", 60), 
            ("🥤 Fanta (330ml)", 60), ("🥤 Diet Coke", 70), ("🍋 Fresh Lime Soda", 90), 
            ("🍹 Virgin Mojito", 140), ("🍹 Blue Lagoon Mocktail", 150), ("🧋 Cold Coffee", 150), 
            ("🧋 Cold Coffee w/ Ice Cream", 180), ("🥤 Chocolate Milkshake", 160), ("🥤 Strawberry Milkshake", 150), 
            ("🥤 Vanilla Milkshake", 140), ("🥤 Oreo Shake", 180), ("🥭 Mango Shake", 160), 
            ("☕ Masala Chai", 40), ("☕ Espresso Coffee", 90), ("☕ Cappuccino", 120), 
            ("☕ Cafe Latte", 130), ("🧋 Iced Peach Tea", 140)
        ]
    }

    for category_name, items in menu_data.items():
        category_obj, created = Category.objects.get_or_create(name=category_name)
        
        for food_name, price in items:
            FoodItem.objects.create( 
                name=food_name,
                category=category_obj,
                description=f"Delicious and fresh {food_name}. Best in town!",
                price=price,
                is_available=True
            )
            
    print("✅ ")

if __name__ == '__main__':
    seed_data()