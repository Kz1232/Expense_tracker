from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):  # For adding extra field as per the need
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Added unique related names to avoid conflicts with Django’s default User model
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_group", 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  
        blank=True
    )

    def __str__(self):
        return self.username
