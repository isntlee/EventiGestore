from .views import EventList
from django.urls import path

app_name = 'events_api'

urlpatterns = [
    path('events/', EventList.as_view({'get': 'list', 'post': 'create'})),
    path('events/<slug:pk>/', EventList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('search/', EventList.as_view({'get': 'retrieve'})),
]