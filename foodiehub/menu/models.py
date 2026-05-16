from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class FoodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_available = models.BooleanField(default=True)
    # इमेज के लिए हम बाद में सेटिंग्स करेंगे, अभी बेसिक रखते हैं

    def __str__(self):
        return self.name

# ... आपका पुराना कोड ...

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} loves {self.food_item.name}"
# Create your models here.
