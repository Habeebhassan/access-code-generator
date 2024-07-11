from django.contrib import admin

from django.contrib import admin
from .models import Resident, Landlord

# Register the Resident model with the Django admin interface
admin.site.register(Resident)

# Register the Landlord model with the Django admin interface
admin.site.register(Landlord)
