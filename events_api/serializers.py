from rest_framework import serializers
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'description', 'slug', 'start_date', 'end_date', 'creator', 'attendees', 'full')