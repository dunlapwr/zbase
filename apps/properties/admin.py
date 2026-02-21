from django.contrib import admin

from .models import Lease, Property, Unit


class UnitInline(admin.TabularInline):
    model = Unit
    extra = 0


class LeaseInline(admin.TabularInline):
    model = Lease
    extra = 0


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "state", "property_type", "is_active")
    list_filter = ("property_type", "state", "is_active")
    inlines = [UnitInline]


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("label", "building", "bedrooms", "rent_amount", "is_active")
    list_filter = ("is_active",)
    inlines = [LeaseInline]


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ("tenant_name", "unit", "rent_amount", "start_date", "end_date")
    list_filter = ("start_date",)
