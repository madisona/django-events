
from django.contrib import admin

from events import models

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'location')
    

admin.site.register(models.Event, EventAdmin)