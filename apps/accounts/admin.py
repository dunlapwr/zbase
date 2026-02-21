from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Household


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "role", "household")
    list_filter = ("role", "household")
    fieldsets = UserAdmin.fieldsets + (
        ("ZHub Profile", {"fields": ("phone", "role", "avatar_url", "household")}),
    )


@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
