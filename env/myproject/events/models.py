from django.db import models
from django.contrib.auth.models import User

# The models are given below

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    hosted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"

class User(models.Model):
    ID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    typ = models.IntegerField()