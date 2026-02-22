from .models import Studio


def active_studios(request):
    """Make the list of active studios available to all templates (for sidebar)."""
    if request.user.is_authenticated:
        return {"sidebar_studios": Studio.objects.filter(is_active=True).order_by("name")}
    return {}
