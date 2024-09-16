# accounts/urls.py
from django.urls import path,include
from .views import signup,home

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', home, name='home'),  # Use the function-based view
    path("accounts/",include("django.contrib.auth.urls"))
    
]
