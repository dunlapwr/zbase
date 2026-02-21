from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LeaseForm, PropertyForm, UnitForm
from .models import Lease, Property, Unit


def _get_household(user):
    """Return the user's household or None."""
    return user.household


@login_required
def property_list(request):
    """Properties portfolio — shows all properties for the user's household."""
    household = _get_household(request.user)
    if household:
        properties = Property.objects.filter(household=household, is_active=True)
    else:
        properties = Property.objects.none()

    return render(request, "properties/list.html", {
        "properties": properties,
        "breadcrumbs": [{"label": "Properties", "url": ""}],
    })


@login_required
def property_add(request):
    """Create a new property."""
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            prop = form.save(commit=False)
            household = _get_household(request.user)
            if not household:
                messages.error(request, "You must belong to a household to add properties.")
                return redirect("properties:list")
            prop.household = household
            prop.save()
            messages.success(request, f'Property "{prop.address}" added.')
            return redirect("properties:detail", pk=prop.pk)
    else:
        form = PropertyForm()

    return render(request, "properties/add.html", {
        "form": form,
        "breadcrumbs": [
            {"label": "Properties", "url": "/properties/"},
            {"label": "Add Property", "url": ""},
        ],
    })


@login_required
def property_detail(request, pk):
    """View a single property with its units and leases."""
    household = _get_household(request.user)
    prop = get_object_or_404(Property, pk=pk, household=household)
    units = prop.units.all().prefetch_related("leases")

    return render(request, "properties/detail.html", {
        "property": prop,
        "units": units,
        "breadcrumbs": [
            {"label": "Properties", "url": "/properties/"},
            {"label": prop.address, "url": ""},
        ],
    })


@login_required
def property_edit(request, pk):
    """Edit an existing property."""
    household = _get_household(request.user)
    prop = get_object_or_404(Property, pk=pk, household=household)

    if request.method == "POST":
        form = PropertyForm(request.POST, instance=prop)
        if form.is_valid():
            form.save()
            messages.success(request, "Property updated.")
            return redirect("properties:detail", pk=prop.pk)
    else:
        form = PropertyForm(instance=prop)

    return render(request, "properties/edit.html", {
        "form": form,
        "property": prop,
        "breadcrumbs": [
            {"label": "Properties", "url": "/properties/"},
            {"label": prop.address, "url": f"/properties/{prop.pk}/"},
            {"label": "Edit", "url": ""},
        ],
    })


@login_required
def property_delete(request, pk):
    """Soft-delete a property (set is_active=False)."""
    household = _get_household(request.user)
    prop = get_object_or_404(Property, pk=pk, household=household)

    if request.method == "POST":
        prop.is_active = False
        prop.save()
        messages.success(request, f'Property "{prop.address}" removed.')
        return redirect("properties:list")

    return render(request, "properties/confirm_delete.html", {
        "property": prop,
        "breadcrumbs": [
            {"label": "Properties", "url": "/properties/"},
            {"label": prop.address, "url": f"/properties/{prop.pk}/"},
            {"label": "Delete", "url": ""},
        ],
    })


# ── Unit views ──


@login_required
def unit_add(request, property_pk):
    """Add a unit to a property."""
    household = _get_household(request.user)
    prop = get_object_or_404(Property, pk=property_pk, household=household)

    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.building = prop
            unit.save()
            messages.success(request, f'Unit "{unit.label}" added.')
            return redirect("properties:detail", pk=prop.pk)
    else:
        form = UnitForm()

    return render(request, "properties/unit_form.html", {
        "form": form,
        "property": prop,
        "breadcrumbs": [
            {"label": "Properties", "url": "/properties/"},
            {"label": prop.address, "url": f"/properties/{prop.pk}/"},
            {"label": "Add Unit", "url": ""},
        ],
    })


@login_required
def unit_edit(request, property_pk, unit_pk):
    """Edit a unit."""
    household = _get_household(request.user)
    prop = get_object_or_404(Property, pk=property_pk, household=household)
    unit = get_object_or_404(Unit, pk=unit_pk, building=prop)

    if request.method == "POST":
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            messages.success(request, f'Unit "{unit.label}" updated.')
            return redirect("properties:detail", pk=prop.pk)
    else:
        form = UnitForm(instance=unit)

    return render(request, "properties/unit_form.html", {
        "form": form,
        "property": prop,
        "unit": unit,
        "breadcrumbs": [
            {"label": "Properties", "url": "/properties/"},
            {"label": prop.address, "url": f"/properties/{prop.pk}/"},
            {"label": f"Edit {unit.label}", "url": ""},
        ],
    })


@login_required
def unit_delete(request, property_pk, unit_pk):
    """Delete a unit."""
    household = _get_household(request.user)
    prop = get_object_or_404(Property, pk=property_pk, household=household)
    unit = get_object_or_404(Unit, pk=unit_pk, building=prop)

    if request.method == "POST":
        label = unit.label
        unit.delete()
        messages.success(request, f'Unit "{label}" deleted.')
        return redirect("properties:detail", pk=prop.pk)

    return render(request, "properties/confirm_delete_unit.html", {
        "property": prop,
        "unit": unit,
        "breadcrumbs": [
            {"label": "Properties", "url": "/properties/"},
            {"label": prop.address, "url": f"/properties/{prop.pk}/"},
            {"label": f"Delete {unit.label}", "url": ""},
        ],
    })


# ── Lease views ──


@login_required
def lease_add(request, property_pk, unit_pk):
    """Add a lease to a unit."""
    household = _get_household(request.user)
    prop = get_object_or_404(Property, pk=property_pk, household=household)
    unit = get_object_or_404(Unit, pk=unit_pk, building=prop)

    if request.method == "POST":
        form = LeaseForm(request.POST)
        if form.is_valid():
            lease = form.save(commit=False)
            lease.unit = unit
            lease.save()
            messages.success(request, f"Lease for {lease.tenant_name} added.")
            return redirect("properties:detail", pk=prop.pk)
    else:
        form = LeaseForm(initial={"rent_amount": unit.rent_amount})

    return render(request, "properties/lease_form.html", {
        "form": form,
        "property": prop,
        "unit": unit,
        "breadcrumbs": [
            {"label": "Properties", "url": "/properties/"},
            {"label": prop.address, "url": f"/properties/{prop.pk}/"},
            {"label": f"New Lease — {unit.label}", "url": ""},
        ],
    })


@login_required
def lease_edit(request, property_pk, unit_pk, lease_pk):
    """Edit a lease."""
    household = _get_household(request.user)
    prop = get_object_or_404(Property, pk=property_pk, household=household)
    unit = get_object_or_404(Unit, pk=unit_pk, building=prop)
    lease = get_object_or_404(Lease, pk=lease_pk, unit=unit)

    if request.method == "POST":
        form = LeaseForm(request.POST, instance=lease)
        if form.is_valid():
            form.save()
            messages.success(request, "Lease updated.")
            return redirect("properties:detail", pk=prop.pk)
    else:
        form = LeaseForm(instance=lease)

    return render(request, "properties/lease_form.html", {
        "form": form,
        "property": prop,
        "unit": unit,
        "lease": lease,
        "breadcrumbs": [
            {"label": "Properties", "url": "/properties/"},
            {"label": prop.address, "url": f"/properties/{prop.pk}/"},
            {"label": f"Edit Lease — {unit.label}", "url": ""},
        ],
    })
