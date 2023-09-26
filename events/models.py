from django.db import models
from accounts.models import User
from django_extensions.db.fields import AutoSlugField


class Event(models.Model):

    class EventObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(active=False)
        
    name = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    slug = AutoSlugField(populate_from='name')
    attendees = models.ManyToManyField(User, related_name='events_attending')
    creator = models.ForeignKey(User, related_name='created_events', on_delete=models.CASCADE)
    full = models.BooleanField(default=False)  

    # Let's reconsider these two below..  
    objects = models.Manager()
    eventobjects = EventObjects()

    class Meta:
        ordering = ('start_date',)

    def __str__(self):
        return self.name 
