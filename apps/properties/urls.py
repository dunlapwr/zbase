from django.urls import path

from . import views

app_name = "properties"

urlpatterns = [
    path("", views.property_list, name="list"),
    path("add/", views.property_add, name="add"),
    path("<int:pk>/", views.property_detail, name="detail"),
    path("<int:pk>/edit/", views.property_edit, name="edit"),
    path("<int:pk>/delete/", views.property_delete, name="delete"),
    # Units
    path("<int:property_pk>/units/add/", views.unit_add, name="unit_add"),
    path("<int:property_pk>/units/<int:unit_pk>/edit/", views.unit_edit, name="unit_edit"),
    path("<int:property_pk>/units/<int:unit_pk>/delete/", views.unit_delete, name="unit_delete"),
    # Leases
    path("<int:property_pk>/units/<int:unit_pk>/leases/add/", views.lease_add, name="lease_add"),
    path("<int:property_pk>/units/<int:unit_pk>/leases/<int:lease_pk>/edit/", views.lease_edit, name="lease_edit"),
]
