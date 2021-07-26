from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from user.enums import Gender, Role


class UserManager(BaseUserManager):

    def _create_user(self, **kwargs):
        user = self.model(**kwargs)
        user.set_password(kwargs.get('password'))
        user.save(using=self._db)
        return user

    def create_user(self, **kwargs):
        kwargs['is_active'] = True
        return self._create_user(**kwargs)

    def create_superuser(self, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(**kwargs)


class User(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=50)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    age = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(18), MaxValueValidator(100)),
    )
    gender = models.CharField(choices=Gender.choices(), max_length=6)
    birthday = models.DateTimeField(null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(max_length=12, choices=Role.choices())

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "password",
        "username",
        "age",
        "gender",
        "role",
    ]

    objects = UserManager()

    def __str__(self):
        return self.email
