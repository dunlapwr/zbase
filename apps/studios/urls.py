from django.urls import path

from . import views

app_name = "studios"

urlpatterns = [
    path("", views.studio_list, name="list"),
    path("combined/", views.studio_combined, name="combined"),
    path("<slug:slug>/", views.studio_detail, name="detail"),
]
