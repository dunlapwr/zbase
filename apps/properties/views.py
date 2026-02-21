from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def property_list(request):
    """Properties portfolio — stub for Phase 3."""
    return render(request, "properties/list.html", {
        "breadcrumbs": [{"label": "Properties", "url": ""}],
    })


@login_required
def property_add(request):
    """Add property form — stub for Phase 3."""
    return render(request, "properties/add.html", {
        "breadcrumbs": [
            {"label": "Properties", "url": "/properties/"},
            {"label": "Add Property", "url": ""},
        ],
    })
