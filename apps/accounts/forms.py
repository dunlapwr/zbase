from django import forms

from .models import CustomUser


class UserProfileForm(forms.ModelForm):
    """Form for editing user profile on the settings page."""

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "phone"]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-emerald-500 focus:ring-emerald-500",
            }),
            "last_name": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-emerald-500 focus:ring-emerald-500",
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-emerald-500 focus:ring-emerald-500",
            }),
            "phone": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-emerald-500 focus:ring-emerald-500",
            }),
        }
