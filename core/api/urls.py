from django.urls import path, include
from rest_framework import routers
from . import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'room', views.RoomViewSet, basename='rooms')
router.register(r'event', views.EventViewSet, basename='events')
router.register(r'book', views.BookViewSet, basename='books')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]