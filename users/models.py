from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class UserRole(models.TextChoices):
        ADMIN = "admin", "Admin"
        CUSTOMER = "customer", "Customer"

    avatar = models.ImageField(upload_to="images/")
    phone_number = models.CharField(max_length=13, unique=True)
    role = models.CharField("Role", choices=UserRole.choices, max_length=16)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
