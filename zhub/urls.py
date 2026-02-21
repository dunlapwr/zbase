"""
ZHub URL configuration.
"""
from django.contrib import admin
from django.urls import include, path

from apps.dashboard import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("studios/", include("apps.studios.urls")),
    path("properties/", include("apps.properties.urls")),
    path("budget/", include("apps.budget.urls")),
    path("settings/", include("apps.accounts.urls")),
    path("", views.home, name="home"),
]
