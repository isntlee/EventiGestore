from django.contrib import admin
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'full', 'creator')


admin.site.register(models.Event, EventAdmin)