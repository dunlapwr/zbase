"""
Data migration to seed the two studio locations.

This ensures Z Lagree and Z Sculpt exist in every environment
(production, staging, local) without relying on seed_demo.
"""
from django.db import migrations


def create_studios(apps, schema_editor):
    Studio = apps.get_model("studios", "Studio")
    Studio.objects.get_or_create(
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
    Studio.objects.get_or_create(
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


def remove_studios(apps, schema_editor):
    Studio = apps.get_model("studios", "Studio")
    Studio.objects.filter(slug__in=["z-lagree", "z-sculpt"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("studios", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_studios, remove_studios),
    ]
