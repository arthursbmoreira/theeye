from django.db.models import query
from rest_framework import viewsets
from theeyeservice.models import Event

from theeyeservice.serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer