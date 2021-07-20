from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password", "username"]

    def __str__(self):
        return self.email
