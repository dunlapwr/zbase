from django.contrib import admin

from .models import Studio


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "phone", "is_active")
    prepopulated_fields = {"slug": ("name",)}
