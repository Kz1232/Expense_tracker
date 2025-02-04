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


# Space Model
class Space(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spaces_created')
    start_date = models.DateField()
    upto_date = models.DateField()

    def __str__(self):
        return self.name

# UserSpace Model (Mapping Users to Spaces with Roles)
class UserSpace(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Member', 'Member')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spaces')
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name='members')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('user', 'space')

# Expense Model
class Expense(models.Model):
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name='expenses')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_created')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.description} - {self.amount}"

# ExpenseDetails Model
class ExpenseDetail(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='details')
    item_name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item_name} - {self.cost}"

# ExpenseParticipants Model
class ExpenseParticipant(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_participated')

    def __str__(self):
        return f"{self.user.username} in {self.expense.description}"

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message[:30]}..."

# Requests Model
class Request(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_made')
    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name='requests_received')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user.username} requested to join {self.space.name} ({self.status})"



