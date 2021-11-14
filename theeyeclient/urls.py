from django.urls import path
from theeyeclient import views

urlpatterns = [
    path('', views.index),
    path('events/<int:pk>', views.detail_event),
    path('events/', views.events),
]
    