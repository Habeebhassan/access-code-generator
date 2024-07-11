from django.urls import path
from . import views  # Assumes views.py is in the same directory as this urls.py file

urlpatterns = [
    path('generate_code/', views.generate_code, name='generate_code'),
    # Defines a URL pattern using path() function:
    # - 'generate_code/': The URL path to match. When accessed via browser, it will be '/<your_base_url>/generate_code/'.
    # - views.generate_code: The view function that handles this URL pattern, imported from the views module.
    # - name='generate_code': A unique name for this URL pattern, which can be used to refer to it in Django templates and code.
]
