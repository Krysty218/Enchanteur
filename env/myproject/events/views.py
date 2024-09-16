from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event,User
from .serializers import EventSerializer
from django.db.models import Q
from django.http import HttpResponse

# Home page
def home(request):
    logger = request.user
    users = User.objects.filter(username=logger.username)
    for user in users:
        print(f"{user.username}")
    return render(request, 'events/home.html',{'users': users})


# List events


def event_list(request):
    query = request.GET.get('search', '')
    category = request.GET.get('category', '')
    location = request.GET.get('location', '')
    date = request.GET.get('date', '')

    events = Event.objects.all()

    if query:
        events = events.filter(title__icontains=query)
    if category:
        events = events.filter(category__icontains=category)
    if location:
        events = events.filter(location__icontains=location)
    if date:
        events = events.filter(date_time__date=date)

    return render(request, 'events/event_list.html', {'events': events})


# Event details
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})



#searching using default django

def search_events(request):
    query = request.GET.get('search', '')
    category = request.GET.get('category', '')
    location = request.GET.get('location', '')
    date = request.GET.get('date', '')

    events = Event.objects.all()

    if query:
        events = events.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if category:
        events = events.filter(category__icontains=category)
    if location:
        events = events.filter(location__icontains=location)
    if date:
        events = events.filter(date_time__date=date)

    return render(request, 'events/event_list.html', {'events': events})

#wishlist

def wishlist(request):
    # Fetch the user's wishlist items from the database
    # You can adjust this part based on your models and requirements
    wishlist_items = []  # Replace with actual data fetching logic
    return render(request, 'events/wishlist.html', {'wishlist_items': wishlist_items})

