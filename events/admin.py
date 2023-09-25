from django.contrib import admin
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug', 'start_date', 'full', 'creator')


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('__str__','user', 'event')


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Attendee, AttendeeAdmin)