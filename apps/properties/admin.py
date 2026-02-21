from django.contrib import admin

from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "state", "property_type", "is_active")
    list_filter = ("property_type", "state", "is_active")
