from django.db import models

class Event(models.Model):
    session_id = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['session_id', '-timestamp']

class Payload(models.Model):
    host = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    element = models.CharField(max_length=50)
    event = models.OneToOneField(Event, on_delete=models.CASCADE)

class Form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    payload = models.OneToOneField(Payload, on_delete=models.CASCADE)