from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodItem
from django.utils import timezone
from datetime import timedelta

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.food_item.price

class OrderMaster(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')
    delivery_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    estimated_delivery_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        
        if not self.id: 
            self.estimated_delivery_time = timezone.now() + timedelta(minutes=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_amount = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code