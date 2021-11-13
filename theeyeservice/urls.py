from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from theeyeservice import views

router = DefaultRouter()
router.register(r'events', views.EventViewSet)

urlpatterns = [
    path('', include(router.urls))
]