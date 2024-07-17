from django.urls import path
from . import views  # Assumes views.py is in the same directory as this urls.py file

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='resident_dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Defines a URL pattern using path() function:
    # - 'dashboard/': The URL path to match. When accessed via browser, it will be '/<your_base_url>/dashboard/'.
    # - views.dashboard: The view function that handles this URL pattern, imported from the views module.
    # - name='resident_dashboard': A unique name for this URL pattern, which can be used to refer to it in Django templates and code.
]
