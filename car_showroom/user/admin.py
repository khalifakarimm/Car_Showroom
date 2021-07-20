from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "balance")
    list_filter = (
        "email",
        "username",
        "is_active"
    )
    search_fields = (
        "email",
        "username",
    )
