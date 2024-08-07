from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ResidentSignUpForm, ResidentProfileForm
from .models import Resident
from django.contrib import messages


@login_required
def dashboard(request):
    """
    View function for rendering a dashboard with a list of residents.
    """
    residents = Resident.objects.all()
    return render(request, 'residents/dashboard.html', {'residents': residents})

def home(request):
    """
    View function for rendering the home page.
    """
    return render(request, 'home.html')

def resident_signup(request):
    """
    View function for handling user registration.
    """
    if request.method == 'POST':
        resident_form = ResidentSignUpForm(request.POST, request.FILES)
        if resident_form.is_valid():
            resident = resident_form.save(commit=False)
            resident.set_password(resident_form.cleaned_data['password'])
            resident.save()
            return redirect('resident_login')
    else:
        resident_form = ResidentSignUpForm()

    return render(request, 'residents/signup.html', {
        'resident_form': resident_form
    })

def resident_login(request):
    """
    View function for handling user login.
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('resident_profile')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'residents/login.html')

def resident_logout(request):
    """
    View function for handling user logout.
    """
    logout(request)
    return redirect('resident_login')

@login_required
def resident_profile(request):
    """
    View function for resident profile to edit their credentials.
    """

    resident = request.user
    return render(request, 'residents/profile.html', {'resident': resident})
    
    # resident = get_object_or_404(Resident, email=request.user.email)
    # if request.method == 'POST':
    #     form = ResidentProfileForm(request.POST, request.FILES, instance=resident)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('resident_profile')
    # else:
    #     form = ResidentProfileForm(instance=resident)
    # return render(request, 'residents/profile.html', {'resident_profile': form})


# from django.contrib.auth import login, logout,  authenticate
# from .forms import ResidentSignUpForm, LandlordForm
# from .models import Landlord
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import redirect, render

# from .models import Resident
# from .forms import ResidentProfileForm


# @login_required
# def dashboard(request):
#     """
#     View function for rendering a dashboard with a list of residents.

#     Parameters:
#     - request: HTTP request object passed automatically by Django.

#     Returns:
#     - HttpResponse object rendering 'residents/dashboard.html' template with 'residents' context.
#     """
#     print("Accessing dashboard view")
#     residents = Resident.objects.all()
#     """
#     Querying all Resident objects from the database using the ORM (Object-Relational Mapper).
#     'Resident.objects.all()' fetches all rows from the Resident table.

#     Note: Make sure 'Resident' model is properly defined in '.models' file.
#     """

#     return render(request, 'residents/dashboard.html', {'residents': residents})
#     """
#     Rendering the 'residents/dashboard.html' template with context data:
#     - 'residents': QuerySet containing all Resident objects fetched from the database.
#     """

# def home(request):
#     """
#     View function for rendering the home page.

#     Parameters:
#     - request: HTTP request object passed automatically by Django.

#     Returns:
#     - HttpResponse object rendering the 'home.html' template.
#     """
#     return render(request, 'home.html')

# def resident_signup(request):
#     """
#     View function for handling user registration.

#     Parameters:
#     - request: HTTP request object passed automatically by Django.

#     Returns:
#     - HttpResponse object rendering 'residents/signup.html' template with context data.
#     """
#     if request.method == 'POST':
#         # If the form is submitted via POST method
#         resident_form = ResidentSignUpForm(request.POST, request.FILES)
#         # landlord_form = LandlordForm(request.POST)

#         if resident_form.is_valid(): # and landlord_form.is_valid():
#             # If form data is valid, save the user and landlord
#             # landlord = landlord_form.save()
#             resident = resident_form.save(commit=False)
#             # resident.landlord = landlord
#             resident.save()
#             # Redirect to 'resident_dashboard' page after successful registration
#             return redirect('resident_profile')
#     else:
#         # If it's a GET request or any other method, create a new form instance
#         # landlord_form = LandlordForm()
#         resident_form = ResidentSignUpForm()

#     return render(request, 'residents/signup.html', {
#         'resident_form': resident_form
#         # 'landlord_form': landlord_form,
#         })

# def resident_login(request):
#     """
#     View function for handling user login.

#     Parameters:
#     - request: HTTP request object passed automatically by Django.

#     Returns:
#     - HttpResponse object rendering 'residents/login.html' template with context data.
#     """
#     print("Accessing login view")
#     if request.method == 'POST':
#         # If the form is submitted via POST method
#         username = request.POST['username']
#         password = request.POST['password']
#         # Authenticate user credentials
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             # If authentication is successful, log in the user
#             login(request, user)
#             # Redirect to 'resident_dashboard' page after successful login
#             return redirect('resident_profile')
#     # Render the login form template for GET requests or if authentication fails
#     return render(request, 'residents/login.html')

# def resident_logout(request):
#     """
#     View function for handling user logout.

#     Parameters:
#     - request: HTTP request object passed automatically by Django.

#     Returns:
#     - HttpResponseRedirect object redirecting to 'login' page.
#     """
#     logout(request)  # Logs out the user by clearing the session
#     return redirect('resident_login')  # Redirects to the 'login' page after logout

# @login_required
# def resident_profile(request):
#     """
#     View function for resident profile to edit their credentials.
#     """
#     # resident = Resident.objects.get(user=request.user)
#     resident = request.user
#     if request.method == 'POST':
#         form = ResidentProfileForm(request.POST, request.FILES, instance=resident)
#         if form.is_valid():
#             form.save()
#             return redirect('resident_profile')
#     else:
#         form = ResidentProfileForm(instance=resident)
#     return render(request, 'residents/profile.html', {'resident_profile': form})