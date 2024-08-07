from django import forms
from .models import Resident, Landlord

class LandlordForm(forms.ModelForm):
    class Meta:
        model = Landlord
        fields = ['name', 'phone_number']

class ResidentSignUpForm(forms.ModelForm):
    """
    Form for signing up a new Resident. Includes landlord details and password.
    """

    landlord = forms.ModelChoiceField(queryset=Landlord.objects.all(), required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = Resident
        fields = [
            'name', 'email', 'password', 'landlord', 'phone_number', 
            'date_moved_in', 'rent_due_date', 
            'estate_name', 'passport_photo'
        ]
        widgets = {
            'date_moved_in': forms.DateInput(attrs={'type': 'date'}),
            'rent_due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        """
        Save the resident instance and associated landlord if provided
        """
        resident = super().save(commit=False)

        # Save the landlord information
        #landlord_name = self.cleaned_data.get("landlord_name")
        #landlord_phone_number = self.cleaned_data.get("landlord_phone_number")

        # if landlord_name and landlord_phone_number:
        #     landlord, created = Landlord.objects.get_or_create(
        #         name=landlord_name,
        #         phone_number=landlord_phone_number
        #     )
        #     resident.landlord = landlord

        # # Set the email and password
        # resident.email = self.cleaned_data['email']
        # resident.set_password(self.cleaned_data['password'])

        resident.set_password(self.cleaned_data['password'])
        if commit:
            resident.save()

        return resident

class ResidentProfileForm(forms.ModelForm):
    """
    Form for updating Resident profile information.
    """
    class Meta:
        model = Resident
        fields = ['name', 'phone_number', 'date_moved_in', 'rent_due_date', 'estate_name', 'passport_photo']
        widgets = {
            'date_moved_in': forms.DateInput(attrs={'type': 'date'}),
            'rent_due_date': forms.DateInput(attrs={'type': 'date'}),
        }