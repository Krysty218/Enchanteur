
# event_maker/forms.py
from django import forms
from .models import Event
from django.contrib.auth.forms import AuthenticationForm


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'timing', 'area', 'celebrity', 'category','status']

class EventMakerAuthenticationForm(AuthenticationForm):
    def get_success_url(self):
        return '/event_maker/profile/'