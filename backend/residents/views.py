from django.contrib.auth import login, logout,  authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Resident

@login_required
def dashboard(request):
    """
    View function for rendering a dashboard with a list of residents.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object rendering 'residents/dashboard.html' template with 'residents' context.
    """
    print("Accessing dashboard view")
    residents = Resident.objects.all()
    """
    Querying all Resident objects from the database using the ORM (Object-Relational Mapper).
    'Resident.objects.all()' fetches all rows from the Resident table.

    Note: Make sure 'Resident' model is properly defined in '.models' file.
    """

    return render(request, 'residents/dashboard.html', {'residents': residents})
    """
    Rendering the 'residents/dashboard.html' template with context data:
    - 'residents': QuerySet containing all Resident objects fetched from the database.
    """
def home(request):
    """
    View function for rendering the home page.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object rendering the 'home.html' template.
    """
    return render(request, 'home.html')

def resident_signup(request):
    """
    View function for handling user registration.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object rendering 'residents/register.html' template with context data.
    """
    if request.method == 'POST':
        # If the form is submitted via POST method
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # If form data is valid, save the user
            user = form.save()
            # Log in the user
            login(request, user)
            # Redirect to 'resident_dashboard' page after successful registration
            return redirect('resident_dashboard')
    else:
        # If it's a GET request or any other method, create a new form instance
        form = UserCreationForm()
    return render(request, 'residents/signup.html', {'form': form})

def resident_login(request):
    """
    View function for handling user login.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object rendering 'residents/login.html' template with context data.
    """
    print("Accessing login view")
    if request.method == 'POST':
        # If the form is submitted via POST method
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If authentication is successful, log in the user
            login(request, user)
            # Redirect to 'resident_dashboard' page after successful login
            return redirect('resident_dashboard')
    # Render the login form template for GET requests or if authentication fails
    return render(request, 'residents/login.html')

def resident_logout(request):
    """
    View function for handling user logout.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponseRedirect object redirecting to 'login' page.
    """
    logout(request)  # Logs out the user by clearing the session
    return redirect('resident_login')  # Redirects to the 'login' page after logout
