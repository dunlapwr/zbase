from django.db import models
from django.utils import timezone


class Property(models.Model):
    """Rental property belonging to a household."""

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
    monthly_mortgage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "properties"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.address}, {self.city} {self.state}"

    @property
    def total_monthly_rent(self):
        return sum(
            unit.rent_amount for unit in self.units.all() if unit.rent_amount
        )

    @property
    def occupied_units(self):
        today = timezone.now().date()
        return self.units.filter(
            leases__start_date__lte=today,
            leases__end_date__gte=today,
        ).distinct().count()

    @property
    def unit_count(self):
        return self.units.count()

    @property
    def occupancy_display(self):
        total = self.unit_count
        if total == 0:
            return "No units"
        return f"{self.occupied_units}/{total}"


class Unit(models.Model):
    """A rentable unit within a property (e.g. Unit A, Unit 1, or the whole house)."""

    building = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="units",
    )
    label = models.CharField(
        max_length=50,
        help_text='e.g. "Unit A", "Suite 101", or "Main" for single-family',
    )
    bedrooms = models.PositiveSmallIntegerField(default=0)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, default=1)
    sq_ft = models.PositiveIntegerField(default=0, blank=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["label"]
        unique_together = [("building", "label")]

    def __str__(self):
        return f"{self.building.address} — {self.label}"

    @property
    def current_lease(self):
        today = timezone.now().date()
        return self.leases.filter(
            start_date__lte=today,
            end_date__gte=today,
        ).first()

    @property
    def is_occupied(self):
        return self.current_lease is not None


class Lease(models.Model):
    """A lease agreement for a unit."""

    STATUS_CHOICES = [
        ("active", "Active"),
        ("upcoming", "Upcoming"),
        ("expired", "Expired"),
    ]

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="leases",
    )
    tenant_name = models.CharField(max_length=200)
    tenant_email = models.EmailField(blank=True)
    tenant_phone = models.CharField(max_length=20, blank=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.tenant_name} — {self.unit}"

    @property
    def status(self):
        today = timezone.now().date()
        if self.start_date > today:
            return "upcoming"
        if self.end_date < today:
            return "expired"
        return "active"

    @property
    def monthly_rent(self):
        return self.rent_amount
