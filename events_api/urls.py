from .views import EventList, RegisterForEventView
from django.urls import path

app_name = 'events_api'

urlpatterns = [
    path('events/', EventList.as_view({'get': 'list', 'post': 'create'})),
    path('events/<slug:pk>/', EventList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('events/<slug:pk>/register_toggle/', RegisterForEventView.as_view({'get': 'post'})),
    path('search/', EventList.as_view({'get': 'retrieve'})),
]