from django import forms
from .models import SecurityPersonnel


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SecurityPersonnel

class SecuritySignUpForm(forms.ModelForm):
    """
    Form for security personnel sign-up.

    Fields:
    - name: Name of the security personnel.
    - company_name: Name of the company the security personnel belongs to.
    - passport_photo: Passport photo of the security personnel.
    - nin_number: National Identification Number (NIN) of the security personnel.
    - phone_number: Phone number of the security personnel.
    - registration_code: Unique registration code of the security personnel.
    """
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = SecurityPersonnel
        fields = ['email', 'name', 'password', 'company_name', 'passport_photo', 'nin_number', 'phone_number']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        security_personnel = super().save(commit=False)
        security_personnel.set_password(self.cleaned_data["password1"])
        if commit:
            security_personnel.save()
        return security_personnel




# class SecuritySignUpForm(forms.ModelForm):
    
#     """
#     Form for security personnel sign-up, inheriting from Django's UserCreationForm.

#     Fields:
#     - username: Username for the security personnel.
#     - password1: Password for the security personnel.
#     - password2: Password confirmation.
#     - name: Name of the security personnel.
#     - company_name: Name of the company the security personnel belongs to.
#     - passport_photo: Passport photo of the security personnel.
#     - nin_number: National Identification Number (NIN) of the security personnel.
#     - phone_number: Phone number of the security personnel.
#     - registration_code: Unique registration code of the security personnel.
#     """

#     class Meta:
#         model = SecurityPersonnel
#         fields = [
#         'name', 'company_name', 'passport_photo', 
#         'nin_number', 'phone_number', 'registration_code'
#         ]
#         # Specifying the fields to be included in the form from the SecurityPersonnel model

