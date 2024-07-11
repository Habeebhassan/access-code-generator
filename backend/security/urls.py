from django.urls import path
from . import views  # Assumes views.py is in the same directory as this urls.py file

urlpatterns = [
    path('dashboard/', views.dashboard, name='security_dashboard'),
    # Defines a URL pattern using path() function:
    # - 'dashboard/': The URL path to match. When accessed via browser, it will be '/<your_base_url>/dashboard/'.
    # - views.dashboard: The view function that handles this URL pattern, imported from the views module.
    # - name='security_dashboard': A unique name for this URL pattern, which can be used to refer to it in Django templates and code.
]
