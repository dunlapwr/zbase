from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserProfileForm


@login_required
def settings_profile(request):
    """User profile settings page."""
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("accounts:settings")
    else:
        form = UserProfileForm(instance=request.user)

    # Get household members
    household_members = []
    if request.user.household:
        household_members = request.user.household.members.exclude(pk=request.user.pk)

    return render(request, "settings/profile.html", {
        "form": form,
        "household_members": household_members,
        "breadcrumbs": [{"label": "Settings", "url": ""}],
    })
