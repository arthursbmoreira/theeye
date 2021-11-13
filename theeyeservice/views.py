from django.db.models import query
from rest_framework import viewsets
from theeyeservice.models import Event
import logging

from datetime import datetime

from theeyeservice.serializers import EventSerializer

logger = logging.getLogger(__name__)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        session_id = self.request.query_params.get('session_id')
        category = self.request.query_params.get('category')
        timeframe_init = self.request.query_params.get('timeframe_init')
        timeframe_end = self.request.query_params.get('timeframe_end')

        queryset = Event.objects.all()
        if session_id: queryset = queryset.filter(session_id=session_id)
        if category: queryset = queryset.filter(category=category)
        
        if timeframe_init:
            try:
                timeframe_init = datetime.fromisoformat(timeframe_init)                
                queryset = queryset.filter(timestamp__gte=timeframe_init)
            except ValueError:
                logger.error('Wrong date format for timeframe_init.')

        if timeframe_end:
            try:
                timeframe_end = datetime.fromisoformat(timeframe_end)                
                queryset = queryset.filter(timestamp__lte=timeframe_end)
            except ValueError:
                logger.error('Wrong date format for timeframe_end.')

        return queryset