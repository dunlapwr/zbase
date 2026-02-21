from django.db import models


class Studio(models.Model):
    """Fitness studio location — full implementation in Phase 2."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=200, blank=True)
    mariana_tek_id = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
