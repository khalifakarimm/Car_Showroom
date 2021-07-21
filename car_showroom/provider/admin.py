from django.contrib import admin

from .models import Car, Provider, Manufacturer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "carcase",
        "state",
        "price",
        "production_date",
    )
    list_filter = (
        "manufacturer__name",
        "model",
        "is_active",
    )
    search_fields = (
        "manufacturer__name",
        "model",
        "carcase",
        "state",
    )


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "name",
        "foundation_time",
    )
    list_filter = (
        "cars",
        "is_active",
        "showrooms",
    )
    search_fields = (
        "name",
        "cars__model",
        "cars__state",
        "cars__carcase",
        "cars__manufacturer__name",
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "name",
        "location",
        "foundation_time",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)
