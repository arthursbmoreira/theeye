from django.urls import path, include
from theeyeservice import views

event_list = views.EventViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
event_detail = views.EventViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [    
    path('events/', event_list, name='event-list'),
    path('events/<int:pk>/', event_detail, name='event-detail'),
]