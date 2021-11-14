from rest_framework import viewsets
from theeyeservice.models import Event
import logging

from datetime import datetime

from theeyeservice.serializers import EventSerializer

logger = logging.getLogger(__name__)

class EventViewSet(viewsets.ModelViewSet):
    """
    Using ModelViewSets will handle most the work of defining crud methods and defining the urls.
    Events will be exposed using the best practices for api design.
    Definig the HTTP verb will define the behavior
    HTTP GET ex1: localhost:8000/api/events/ will return all the events
    HTTP GET ex2: localhost:8000/api/events/1 will return the event with id 1
    HTTP POST ex: localhost:8000/api/events/ accepts a JSON body to be persisted
    POST body ex:   {
                    "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
                    "category": "page interaction",
                    "name": "pageview",
                    "data": {
                        "host": "www.consumeraffairs.com",
                        "path": "/",
                    },
                    "timestamp": "2021-01-01 09:15:27.243860"
                }
    It is possible to filter events by sessio_id, category, timeframe_init and timeframe_end, passing any of them as query parameters.
    Ex1: localhost:8000/api/events/?session_id=e2085be5-9137-4e4e-80b5-f1ffddc25424
    Ex2: localhost:8000/api/events/?session_id=e2085be5-9137-4e4e-80b5-f1ffddc25424&category=page interaction
    Ex3: localhost:8000/api/events/?timeframe_init=2020-01-01&timeframe_end=2021-01-01T09:15:27.243860-04:00
    Ex4: localhost:8000/api/events/?timeframe_init=2020-01-01
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        logger.info('Querying events - start')
        queryset = self.queryset

        session_id = self.request.query_params.get('session_id')
        if session_id:
            logger.info('Querying by session_id')
            queryset = queryset.filter(session_id=session_id)

        category = self.request.query_params.get('category')
        if category:
            logger.info('Querying by category')
            queryset = queryset.filter(category=category)

        timeframe_init = self.request.query_params.get('timeframe_init')
        if timeframe_init:
            try:
                logger.info('Querying by timeframe_init')
                timeframe_init = datetime.fromisoformat(timeframe_init)                
                queryset = queryset.filter(timestamp__gte=timeframe_init)
            except ValueError:
                logger.error('Wrong date format for timeframe_init.')

        timeframe_end = self.request.query_params.get('timeframe_end')        
        if timeframe_end:
            try:
                logger.info('Querying by timeframe_end')
                timeframe_end = datetime.fromisoformat(timeframe_end)                
                queryset = queryset.filter(timestamp__lte=timeframe_end)
            except ValueError:
                logger.error('Wrong date format for timeframe_end.')

        logger.info('Querying events - end')
        return queryset