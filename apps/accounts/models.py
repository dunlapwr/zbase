from django.contrib.auth.models import AbstractUser
from django.db import models


class Household(models.Model):
    """Groups users who share financial data (e.g. a married couple)."""

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    """Extended user with household membership and profile fields."""

    ROLE_CHOICES = [
        ("owner", "Owner"),
        ("viewer", "Viewer"),
    ]

    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="owner")
    avatar_url = models.URLField(blank=True)
    household = models.ForeignKey(
        Household,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="members",
    )

    def __str__(self):
        return self.get_full_name() or self.username
