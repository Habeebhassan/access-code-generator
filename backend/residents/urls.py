from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import resident_profile


from . import views  # Assumes views.py is in the same directory as this urls.py file

urlpatterns = [
    #path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='resident_dashboard'),
    path('signup/', views.resident_signup, name='resident_signup'),
    path('login/', views.resident_login, name='resident_login'),
    path('logout/', views.resident_logout, name='resident_logout'),
    path('profile/', resident_profile, name='resident_profile'),
    # Defines a URL pattern using path() function:
    # - 'dashboard/': The URL path to match. When accessed via browser, it will be '/<your_base_url>/dashboard/'.
    # - views.dashboard: The view function that handles this URL pattern, imported from the views module.
    # - name='resident_dashboard': A unique name for this URL pattern, which can be used to refer to it in Django templates and code.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
