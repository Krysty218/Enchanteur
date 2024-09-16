
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import EventManager
from django.contrib.auth import login as login

def event_manager_signup_m(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            EventManager.objects.create(user=user, organization_name=request.POST.get('organization_name'))
            login(request, user)
            return redirect('create_event')
    else:
        form = UserCreationForm()

    return render(request, 'event_maker/signup_m.html', {'form': form})

from django.contrib.auth.decorators import login_required as login_required
from django.shortcuts import render, redirect
from .forms import EventForm
'''
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.event_manager = request.user.eventmanager
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'event_maker/create_event.html', {'form': form})
'''
'''
# event_maker/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import EventManager

def event_manager_signup_m(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            EventManager.objects.create(user=user, organization_name=request.POST.get('organization_name'))
            login(request, user)  # Log in the user after signup_m
            return redirect('create_event')  # Redirect to the event creation page
    else:
        form = UserCreationForm()

    return render(request, 'event_maker/signup_m.html', {'form': form})

'''

'''
# event_maker/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import EventManager

def event_manager_signup_m(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            organization_name = request.POST.get('organization_name')  # Get the organization name
            # Create an EventManager associated with this user
            EventManager.objects.create(user=user, organization_name=organization_name)
            event.save()
            login(request, user)  # Automatically log in the user after signup_m
            return redirect('create_event')  # Redirect to event creation page
    else:
        form = UserCreationForm()

    return render(request, 'event_maker/signup_m.html', {'form': form})

'''
# event_maker/views.py
from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.decorators import login_required as login_required
from .forms import EventForm

# event_maker/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required as login_required
from .models import Event, EventManager
from .forms import EventForm

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.manager = EventManager.objects.get(user=request.user)  # Assign logged-in manager
            event.save()
            return redirect('event_manager_profile')  # Redirect to profile after creation
    else:
        form = EventForm()

    return render(request, 'event_maker/create_event.html', {'form': form})

# event_maker/views.py


# event_maker/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required as login_required
from .models import EventManager, Event

@login_required
def event_manager_profile(request):
    # Get the EventManager instance linked to the logged-in user
    event_manager = EventManager.objects.get(user=request.user)
    
    # Get all event_maker created by the logged-in event manager
    event_maker = Event.objects.filter(manager=event_manager)

    context = {
        'event_manager': event_manager,
        'event_maker': event_maker,
    }
    return render(request, 'event_maker/profile.html', context)
'''
# event_maker/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, EventManager
from .forms import EventForm

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.manager = EventManager.objects.get(user=request.user)
            event.save()
            return redirect('event_manager_profile')
    else:
        form = EventForm()

    return render(request, 'event_maker/create_event.html', {'form': form})
'''


# event_maker/views.py
# event_maker/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required as login_required
from .models import Event
from .forms import EventForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect



@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, manager__user=request.user)  # Ensure the event belongs to the logged-in manager
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_manager_profile')  # Redirect back to profile after editing
    else:
        form = EventForm(instance=event)  # Pre-fill the form with current event data

    return render(request, 'event_maker/edit_event.html', {'form': form, 'event': event})

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

class EventMakerLoginView(LoginView):
    template_name = 'event_maker/login.html'

    def get_redirect_url(self):
        return '/event_maker/profile/'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', '/event_maker/profile/')
                return redirect(next_url)
    else:
        form = AuthenticationForm()
    
    return render(request, 'event_maker/login.html', {'form': form})