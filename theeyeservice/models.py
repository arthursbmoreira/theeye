from django.db import models
from .validators import validate_event_date_not_future

class Event(models.Model):
    session_id = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(validators=[validate_event_date_not_future])

    class Meta:
        ordering = ['session_id', '-timestamp']

class Payload(models.Model):
    host = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    element = models.CharField(max_length=50, blank=True, null=True)
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='data')

class Form(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    payload = models.OneToOneField(Payload, on_delete=models.CASCADE)