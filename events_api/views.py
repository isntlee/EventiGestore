from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Q
from events.models import Event
from .permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer
from datetime import datetime

import pytz


class EventList(viewsets.ViewSet):
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'creator__username']
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        print('\n\n Here.. #1 \n\n')
        queryset = Event.objects.all()
        search_param = self.request.query_params.get('search')
        if search_param:
            queryset = queryset.filter(Q(name__icontains=search_param)|Q(creator__username__iexact=search_param))
        return queryset

    def list(self, request):
        req_obj = request.authenticators
        print('\n\n', req_obj, '\n\n')
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, **kwargs):
        item = self.kwargs.get('pk')
        event = get_object_or_404(self.get_queryset(), slug=item)
        serializer = self.serializer_class(event)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return ValidationError(serializer.errors)

    def update(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), slug=pk)
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return ValidationError(serializer.errors)
        
    def destroy(self, request, pk=None):
        event = get_object_or_404(self.get_queryset(), slug=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class RegisterForEventView(viewsets.ViewSet):

    def post(self, request, pk=None):
        event = get_object_or_404(Event, slug=pk)
        user = request.user

        if self.is_future_event(event.start_date):
            if event.attendees.filter(pk=user.pk).exists():
                event.attendees.remove(user)
                message = 'User removed from event'
                status_code = status.HTTP_204_NO_CONTENT
            else:
                event.attendees.add(user)
                message = 'User added to event'
                status_code = status.HTTP_201_CREATED
        else:
            message = 'Unable to access past events'
            status_code = status.HTTP_204_NO_CONTENT

        return Response({'message': message}, status=status_code)

    def is_future_event(self, event_datetime):
        current_time = datetime.now(pytz.timezone('UTC'))
        return event_datetime > current_time