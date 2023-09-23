from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):

    class EventObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(active=False)
        
    name = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    attendees = models.ManyToManyField(User)
    creator = models.ForeignKey(User, related_name='created_events', on_delete=models.CASCADE)
    full = models.BooleanField(default=False)    
    objects = models.Manager()
    eventobjects = EventObjects()

    class Meta:
        ordering = ('start_date',)
    
    def __str__(self):
        return self.name 