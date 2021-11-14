from django.db import models
from django.db.models.fields.related import OneToOneField
from .validators import validate_event_date_not_future

class Event(models.Model):
    session_id = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(validators=[validate_event_date_not_future])
    data = OneToOneField('Payload', on_delete=models.PROTECT)

    class Meta:
        ordering = ['session_id', 'timestamp']

class Payload(models.Model):
    host = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    element = models.CharField(max_length=50, blank=True, default='')
    form = OneToOneField('Form', on_delete=models.PROTECT, blank=True, null=True)

class Form(models.Model):
    first_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')