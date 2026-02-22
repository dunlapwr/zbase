from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Studio


@login_required
def studio_list(request):
    """Studios overview — stub for Phase 2."""
    studios = Studio.objects.filter(is_active=True)
    return render(request, "studios/list.html", {
        "studios": studios,
        "breadcrumbs": [{"label": "Studios", "url": ""}],
    })


@login_required
def studio_detail(request, slug):
    """Individual studio location page."""
    studio = get_object_or_404(Studio, slug=slug)
    return render(request, "studios/detail.html", {
        "studio": studio,
        "breadcrumbs": [
            {"label": "Studios", "url": "/studios/"},
            {"label": studio.name, "url": ""},
        ],
    })


@login_required
def studio_combined(request):
    """Combined view of all studios — stub for Phase 2."""
    return render(request, "studios/combined.html", {
        "breadcrumbs": [
            {"label": "Studios", "url": "/studios/"},
            {"label": "Combined View", "url": ""},
        ],
    })
