"""
Management command to seed demo data for ZHub.

Creates:
- One Household ("Dunlap Household")
- Two users (owner1, owner2) in that household
- Two Studio records (Z Lagree, Z Sculpt)
- Two sample Property records

Usage:
    python manage.py seed_demo
"""
from datetime import date
from decimal import Decimal

from django.core.management.base import BaseCommand

from apps.accounts.models import CustomUser, Household
from apps.properties.models import Property
from apps.studios.models import Studio


class Command(BaseCommand):
    help = "Seed the database with demo data for ZHub"

    def handle(self, *args, **options):
        self.stdout.write("Seeding demo data...")

        # Household
        household, _ = Household.objects.get_or_create(
            name="Dunlap Household",
        )
        self.stdout.write(f"  Household: {household}")

        # Users
        owner1, created = CustomUser.objects.get_or_create(
            username="owner1",
            defaults={
                "email": "owner1@zhub.local",
                "first_name": "Whitney",
                "last_name": "Dunlap",
                "role": "owner",
                "household": household,
            },
        )
        if created:
            owner1.set_password("zhub1234")
            owner1.save()
        self.stdout.write(f"  User: {owner1} ({'created' if created else 'exists'})")

        owner2, created = CustomUser.objects.get_or_create(
            username="owner2",
            defaults={
                "email": "owner2@zhub.local",
                "first_name": "Jordan",
                "last_name": "Dunlap",
                "role": "owner",
                "household": household,
            },
        )
        if created:
            owner2.set_password("zhub1234")
            owner2.save()
        self.stdout.write(f"  User: {owner2} ({'created' if created else 'exists'})")

        # Studios
        zlagree, _ = Studio.objects.get_or_create(
            slug="z-lagree",
            defaults={
                "name": "Z Lagree",
                "location": "Lubbock, TX",
                "address": "4414 82nd Street Suite 115",
                "city": "Lubbock",
                "state": "TX",
                "zip": "79423",
                "phone": "(806) 701-1256",
            },
        )
        self.stdout.write(f"  Studio: {zlagree}")

        zsculpt, _ = Studio.objects.get_or_create(
            slug="z-sculpt",
            defaults={
                "name": "Z Sculpt",
                "location": "Lubbock, TX",
                "address": "2703 26th Street Suite A",
                "city": "Lubbock",
                "state": "TX",
                "zip": "79410",
                "phone": "(806) 701-1141",
            },
        )
        self.stdout.write(f"  Studio: {zsculpt}")

        # Properties
        prop1, _ = Property.objects.get_or_create(
            household=household,
            address="1234 University Ave",
            defaults={
                "city": "Lubbock",
                "state": "TX",
                "zip": "79401",
                "property_type": "single_family",
                "bedrooms": 3,
                "bathrooms": Decimal("2.0"),
                "sq_ft": 1650,
                "purchase_price": Decimal("185000.00"),
                "purchase_date": date(2021, 6, 15),
                "current_value": Decimal("210000.00"),
                "notes": "Near Texas Tech campus, long-term tenant",
            },
        )
        self.stdout.write(f"  Property: {prop1}")

        prop2, _ = Property.objects.get_or_create(
            household=household,
            address="5678 Slide Road",
            defaults={
                "city": "Lubbock",
                "state": "TX",
                "zip": "79414",
                "property_type": "multi_family",
                "bedrooms": 4,
                "bathrooms": Decimal("3.0"),
                "sq_ft": 2200,
                "purchase_price": Decimal("245000.00"),
                "purchase_date": date(2022, 3, 1),
                "current_value": Decimal("275000.00"),
                "notes": "Duplex, both units occupied",
            },
        )
        self.stdout.write(f"  Property: {prop2}")

        self.stdout.write(self.style.SUCCESS("\nDemo data seeded successfully!"))
        self.stdout.write(self.style.SUCCESS("  Login with: owner1 / zhub1234  or  owner2 / zhub1234"))
