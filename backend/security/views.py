from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,  authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from .models import SecurityPersonnel

def security_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('security_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'security/signup.html', {'form': form})

def security_login(request):
    """
    View function for handling security personnel login.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object rendering 'security/login.html' template with context data.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('security_dashboard')  
    return render(request, 'security/login.html')

def security_logout(request):
    """
    View function for handling security personnel logout.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object redirecting to the security login page.
    """
    logout(request)
    return redirect('security_login')

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
