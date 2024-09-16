from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('events/', views.event_list, name='event_list'),  # List of events
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),  # Event details page
    path('search/', views.search_events, name='search_events'),  # Search functionality
]
