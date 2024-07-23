from django import forms
from .models import Resident

class ResidentSignUpForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = [
            'name', 'landlord', 'phone_number', 
            'date_moved_in', 'rent_due_date', 
            'estate_name', 'passport_photo'
        ]
        widgets = {
            'date_moved_in': forms.DateInput(attrs={'type': 'date'}),
            'rent_due_date': forms.DateInput(attrs={'type': 'date'}),
        }