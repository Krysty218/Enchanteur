
from django.urls import path, include
from django.contrib import admin
from .views import create_event,edit_event,event_manager_profile
from django.contrib.auth import views as auth_views
#import edit_event
urlpatterns = [
    path('event_maker/', include('event_maker.urls')),
    path('admin/', admin.site.urls),
]

# event_maker/urls.py
from django.urls import path
from . import views
from .views import EventMakerLoginView


urlpatterns = [
    path('signup_m/', views.event_manager_signup_m, name='event_manager_signup_m'),
    path('create_event/', views.create_event, name='create_event'),
    path('profile/', views.event_manager_profile, name='event_manager_profile'),  # Add this line
    path('event_maker/<int:event_id>/edit/', edit_event, name='edit_event'),  # URL for editing an event
    path('login_m/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login_m'),
    path('event_maker/login_m/', EventMakerLoginView.as_view(), name='event_maker_login'),

]

