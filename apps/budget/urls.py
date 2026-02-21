from django.urls import path

from . import views

app_name = "budget"

urlpatterns = [
    path("", views.budget_overview, name="overview"),
    path("transactions/", views.budget_transactions, name="transactions"),
    path("accounts/", views.budget_accounts, name="accounts"),
]
