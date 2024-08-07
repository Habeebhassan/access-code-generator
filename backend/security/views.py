from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,  authenticate
from django.contrib.auth.decorators import login_required
from .forms import SecuritySignUpForm

#from django.contrib.auth.forms import UserCreationForm
from .models import SecurityPersonnel
from .forms import SecuritySignUpForm
from django.contrib import messages

# def security_signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('security_dashboard')
#     else:
#         form = UserCreationForm()
#     return render(request, 'security/signup.html', {'form': form})

def security_signup(request):
    """
    View function for handling security personnel sign-up.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object rendering 'security/signup.html' template with form context.
    """
    if request.method == 'POST':
        security_form = SecuritySignUpForm(request.POST, request.FILES)
        if security_form.is_valid():
            security_personnel = security_form.save(commit=False)
            security_personnel.set_password(security_form.cleaned_data['password'])
            security_personnel.save()
            # Authenticate and log in the user
            return redirect('security_login')
    else:
        security_form = SecuritySignUpForm()
    return render(request, 'security/signup.html', {'security_form': security_form})
    # Rendering the 'security/signup.html' template with context data: 'form'

def security_login(request):
    """
    View function for handling security personnel login.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object rendering 'security/login.html' template with context data.
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('security_profile')
        else:
            messages.error(request, 'Email or password is incorrect')
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
def security_profile(request):
    """
    View function for displaying the security personnel profile.

    Parameters:
    - request: HTTP request object passed automatically by Django.

    Returns:
    - HttpResponse object rendering 'security/profile.html' template with context data.
    """
    try:
        security_personnel = SecurityPersonnel.objects.get(email=request.user.email)
        return render(request, 'security/profile.html', {
            'security_personnel': security_personnel})
    except SecurityPersonnel.DoesNotExist:
        return render(request, 'security/profile_not_found.html')
        
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

    return render(request, 'security/security_dashboard.html', {'security_personnel': security_personnel})
    """
    Rendering the 'security/dashboard.html' template with context data:
    - 'security_personnel': QuerySet containing all SecurityPersonnel objects fetched from the database.
    """

@login_required
def security_logout(request):
    """
    View function to handle user logout.
    """
    logout(request)
    return redirect('/')
    
