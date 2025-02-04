from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):  # Extends Django's built-in User model
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Add unique related names to avoid conflicts with Django’s default User model
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set", 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  
        blank=True
    )

    def __str__(self):
        return self.username
