from django.db import models


class Property(models.Model):
    """Rental property — full implementation in Phase 3."""

    PROPERTY_TYPE_CHOICES = [
        ("single_family", "Single Family"),
        ("multi_family", "Multi Family"),
        ("condo", "Condo"),
        ("townhouse", "Townhouse"),
        ("commercial", "Commercial"),
    ]

    household = models.ForeignKey(
        "accounts.Household",
        on_delete=models.CASCADE,
        related_name="properties",
    )
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default="single_family")
    bedrooms = models.PositiveSmallIntegerField(default=0)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    sq_ft = models.PositiveIntegerField(default=0)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    purchase_date = models.DateField(null=True, blank=True)
    current_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "properties"

    def __str__(self):
        return f"{self.address}, {self.city} {self.state}"
