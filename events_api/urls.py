from .views import EventList
from django.urls import path

app_name = 'events_api'

urlpatterns = [
    path('events/', EventList.as_view({'get': 'list', 'post': 'create'})),
    path('events/<slug:pk>/', EventList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('events/<int:pk>/register/', views.RegisterForEventView.as_view(), name='register_for_event'),
    path('search/', EventList.as_view({'get': 'retrieve'})),
]