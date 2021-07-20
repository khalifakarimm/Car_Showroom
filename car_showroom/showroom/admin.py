from django.contrib import admin

from .models import (
    ShowroomPurchaseHistory,
    ShowroomSaleHistory,
    Showroom,
    Location,
)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "city",
        "street",
        "building_number",
    )
    list_filter = ("country", "city",)
    search_fields = (
        "country",
        "city",
        "street",
        "building_number",
    )


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "balance",
        "location",
    )
    list_filter = (
        "location__city",
        "is_active",
    )
    search_fields = (
        "name",
        "location__country",
        "location__city",
        "cars__manufacturer__name",
        "customers__email",
    )


@admin.register(ShowroomSaleHistory)
class ShowroomSaleHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "showroom",
        "sold_car",
        "customer",
    )
    list_filter = (
        "sold_car__model",
        "sold_car__manufacturer__name",
        "showroom__name",
    )
    search_fields = (
        "showroom__name",
        "customer__email",
        "sold_car__model",
        "sold_car__state",
        "sold_car__carcase",
        "sold_car__manufacturer__name",
        "showroom__name",
    )


@admin.register(ShowroomPurchaseHistory)
class ShowroomPurchaseHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "bought_car",
        "showroom",
        "provider",
    )
    list_filter = (
        "bought_car__model",
        "bought_car__manufacturer__name",
        "provider__name",
    )
    search_fields = (
        "provider__name",
        "bought_car__model",
        "bought_car__manufacturer__name",
        "showroom__name",
    )
