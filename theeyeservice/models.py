from django.db import models
from django.db.models.fields.related import OneToOneField
from .validators import validate_event_date_not_future

class Event(models.Model):
    session_id = models.TextField()
    category = models.TextField()
    name = models.TextField()
    timestamp = models.DateTimeField(validators=[validate_event_date_not_future])
    data = OneToOneField('Payload', on_delete=models.PROTECT)

    class Meta:
        ordering = ['session_id', 'timestamp']

class Payload(models.Model):
    host = models.TextField()
    path = models.TextField()
    element = models.TextField(blank=True, default='')
    form = OneToOneField('Form', on_delete=models.PROTECT, blank=True, null=True)

class Form(models.Model):
    first_name = models.TextField(blank=True, default='')
    last_name = models.TextField(blank=True, default='')