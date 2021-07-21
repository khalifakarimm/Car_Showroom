from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    location = models.ForeignKey(
        "showroom.Location",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
    )
    foundation_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        related_name="cars",
    )
    model = models.CharField(max_length=50)
    carcase = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    production_date = models.DateTimeField(
        validators=(MinValueValidator(1950), MaxValueValidator(2021))
    )

    def __str__(self):
        return self.model


class Provider(models.Model):
    name = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    foundation_time = models.DateTimeField()
    cars = models.ManyToManyField(
        Car,
        related_name="providers",
    )
    showrooms = models.ManyToManyField(
        "showroom.Showroom",
        related_name="+",
    )

    def __str__(self):
        return self.name
