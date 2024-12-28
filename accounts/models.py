from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member')
    )
    
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default="member")
    
    date_joined = models.DateTimeField(auto_now_add=True)
