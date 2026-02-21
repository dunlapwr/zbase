from django import forms

from .models import Lease, Property, Unit

INPUT_CLASSES = "w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:border-emerald-500 focus:ring-emerald-500"
SELECT_CLASSES = INPUT_CLASSES


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "address", "city", "state", "zip", "property_type",
            "bedrooms", "bathrooms", "sq_ft",
            "purchase_price", "purchase_date", "current_value",
            "monthly_mortgage", "notes",
        ]
        widgets = {
            "address": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "123 Main St"}),
            "city": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "Lubbock"}),
            "state": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "TX", "maxlength": 2}),
            "zip": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "79401"}),
            "property_type": forms.Select(attrs={"class": SELECT_CLASSES}),
            "bedrooms": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0}),
            "bathrooms": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0, "step": "0.5"}),
            "sq_ft": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0}),
            "purchase_price": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0, "step": "0.01", "placeholder": "0.00"}),
            "purchase_date": forms.DateInput(attrs={"class": INPUT_CLASSES, "type": "date"}),
            "current_value": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0, "step": "0.01", "placeholder": "0.00"}),
            "monthly_mortgage": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0, "step": "0.01", "placeholder": "0.00"}),
            "notes": forms.Textarea(attrs={"class": INPUT_CLASSES, "rows": 3, "placeholder": "Optional notes..."}),
        }


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ["label", "bedrooms", "bathrooms", "sq_ft", "rent_amount"]
        widgets = {
            "label": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": 'e.g. "Unit A" or "Main"'}),
            "bedrooms": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0}),
            "bathrooms": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0, "step": "0.5"}),
            "sq_ft": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0}),
            "rent_amount": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0, "step": "0.01", "placeholder": "0.00"}),
        }


class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = [
            "tenant_name", "tenant_email", "tenant_phone",
            "rent_amount", "start_date", "end_date",
            "security_deposit", "notes",
        ]
        widgets = {
            "tenant_name": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "John Doe"}),
            "tenant_email": forms.EmailInput(attrs={"class": INPUT_CLASSES, "placeholder": "tenant@example.com"}),
            "tenant_phone": forms.TextInput(attrs={"class": INPUT_CLASSES, "placeholder": "(555) 123-4567"}),
            "rent_amount": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0, "step": "0.01"}),
            "start_date": forms.DateInput(attrs={"class": INPUT_CLASSES, "type": "date"}),
            "end_date": forms.DateInput(attrs={"class": INPUT_CLASSES, "type": "date"}),
            "security_deposit": forms.NumberInput(attrs={"class": INPUT_CLASSES, "min": 0, "step": "0.01"}),
            "notes": forms.Textarea(attrs={"class": INPUT_CLASSES, "rows": 3, "placeholder": "Optional notes..."}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")
        if start and end and end <= start:
            raise forms.ValidationError("End date must be after start date.")
        return cleaned_data
