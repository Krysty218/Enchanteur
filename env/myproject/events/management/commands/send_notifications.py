from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from events.models import Ticket

class Command(BaseCommand):
    help = 'Send notifications for upcoming events'

    def handle(self, *args, **kwargs):
        # Get all tickets for events happening in the next 24 hours
        upcoming_tickets = Ticket.objects.filter(
            event__date_time__gte=timezone.now(),
            event__date_time__lte=timezone.now() + timezone.timedelta(days=1)
        )
        for ticket in upcoming_tickets:
            send_mail(
                'Upcoming Event Reminder',
                f'Dear {ticket.user.username},\n\nYour event "{ticket.event.title}" is happening soon.',
                'your-email@gmail.com',
                [ticket.user.email],
                fail_silently=False,
            )
