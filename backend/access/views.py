from django.shortcuts import render
from .models import AccessCode
from residents.models import Resident
from django.utils import timezone
from datetime import timedelta
import random
import string
from django.contrib.auth.decorators import login_required

@login_required
def generate_code(request):
    """
    View function for generating an access code for a resident.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object rendering 'access/generate_code.html' template with context data.
    """
    if request.method == "POST":
        # If the form is submitted via POST method
        resident_id = request.POST.get('resident_id')
        # Retrieve the resident ID from POST data
        resident = Resident.objects.get(id=resident_id)
        # Retrieve the Resident object associated with the given ID

        # Generate a random 6-character alphanumeric code
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Set expiration time to 1 day from now
        expires_at = timezone.now() + timedelta(days=1)

        # Create a new AccessCode instance and save it to the database
        access_code = AccessCode.objects.create(code=code, resident=resident, expires_at=expires_at)

        # Render 'access/generate_code.html' template with access_code context
        return render(request, 'access/generate_code.html', {'access_code': access_code})

    # If the request method is not POST (initial GET request)
    residents = Resident.objects.all()
    # Fetch all Resident objects from the database

    # Render 'access/generate_code.html' template with residents context
    return render(request, 'access/generate_code.html', {'residents': residents})
