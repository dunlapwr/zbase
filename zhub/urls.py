"""
ZHub URL configuration.
"""
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

from apps.dashboard import views


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health/", health, name="health"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("studios/", include("apps.studios.urls")),
    path("properties/", include("apps.properties.urls")),
    path("budget/", include("apps.budget.urls")),
    path("settings/", include("apps.accounts.urls")),
    path("", views.home, name="home"),
]
