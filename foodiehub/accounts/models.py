from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # इसे Django के डिफ़ॉल्ट User मॉडल से लिंक कर रहे हैं
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Create your models here.
