from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import SecurityPersonnel

@login_required
def dashboard(request):
    """
    View function for rendering a dashboard with a list of security personnel.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object rendering 'security/dashboard.html' template with 'security_personnel' context.
    """
    security_personnel = SecurityPersonnel.objects.all()
    """
    Querying all SecurityPersonnel objects from the database using the ORM (Object-Relational Mapper).
    'SecurityPersonnel.objects.all()' fetches all rows from the SecurityPersonnel table.

    Note: Make sure 'SecurityPersonnel' model is properly defined in '.models' file.
    """

    return render(request, 'security/dashboard.html', {'security_personnel': security_personnel})
    """
    Rendering the 'security/dashboard.html' template with context data:
    - 'security_personnel': QuerySet containing all SecurityPersonnel objects fetched from the database.
    """
