# event_maker/models.py
from django.db import models
from django.contrib.auth.models import User

class EventManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=100)

    def _str_(self):
        return self.organization_name

class Event(models.Model):
    STATUS_CHOICES = [('scheduled','Scheduled'),('cancelled','Cancelled'),('ended','Ended')]
    title = models.CharField(max_length=200)
    description = models.TextField()
    timing = models.DateTimeField()
    area = models.CharField(max_length=100)
    celebrity = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    manager = models.ForeignKey(EventManager, on_delete=models.CASCADE)  # Link to EventManager
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='scheduled')
    def _str_(self):
        return self.title