
import datetime
from django.db import models

class EventManager(models.Manager):

    def get_upcoming_events(self, num=5):
        today = datetime.date.today()
        return self.filter(start_time__gte=today)[:num]

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    description = models.TextField(blank=True)

    objects = EventManager()

    class Meta(object):
        ordering = ('start_time',)

    def __unicode__(self):
        return unicode(self.name)