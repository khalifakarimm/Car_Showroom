from django_countries.fields import CountryField
from django.db import models

from provider.models import Car


class Location(models.Model):
    country = CountryField()
    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    building_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.country} {self.city} {self.street} {self.building_number}"


class Showroom(models.Model):
    name = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    preferred_model = models.CharField(max_length=50)
    preferred_carcase = models.CharField(max_length=50)
    preferred_state = models.CharField(max_length=50)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, related_name="+", null=True
    )
    available_cars = models.ManyToManyField(
        Car,
        through="ShowroomSaleHistory",
        through_fields=("showroom", "sold_car"),
        related_name="car_showrooms"
    )
    customers = models.ManyToManyField(
        "user.User",
        related_name="car_showrooms",
    )

    providers = models.ManyToManyField(
        "provider.Provider", related_name="car_showrooms"
    )

    def __str__(self):
        return self.name


class ShowroomSaleHistory(models.Model):
    cars_quantity = models.PositiveSmallIntegerField()
    sold_car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name="+",
    )
    customer = models.ForeignKey(
        "user.User",
        on_delete=models.SET_NULL,
        related_name="purchases",
        null=True,
    )
    showroom = models.ForeignKey(
        Showroom, on_delete=models.CASCADE, related_name="sales"
    )

    def __str__(self):
        return self.sold_car


class ShowroomPurchaseHistory(models.Model):
    cars_quantity = models.PositiveSmallIntegerField()
    showroom = models.ForeignKey(
        Showroom, on_delete=models.CASCADE, related_name="purchases"
    )
    bought_car = models.ForeignKey(
        Car, on_delete=models.SET_NULL, related_name="+", null=True
    )
    provider = models.ForeignKey(
        "provider.Provider",
        on_delete=models.SET_NULL,
        related_name="sales",
        null=True,
    )

    def __str__(self):
        return self.bought_car
