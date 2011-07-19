"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import datetime
import re

from django.test import TestCase
from django.template import Template, Context

from events import models

class UpcomingEventsTemplateTagTests(TestCase):

    def test_renders_page_with_upcoming_events(self):
        today = datetime.date.today()
        event1 = models.Event.objects.create(name="Event1", start_time=today + datetime.timedelta(days=1))
        event2 = models.Event.objects.create(name="Event2", start_time=today + datetime.timedelta(days=2))
        models.Event.objects.create(name="Event3", start_time=today + datetime.timedelta(days=3))

        template = Template("""
            {% load event_tags %}
            {% upcoming_events 2 %}
                <ul>
                {% for event in upcoming_events %}
                    <li>{{ event }}
                {% endfor %}
                </ul>
            {% endupcoming_events %}

        """)

        context = Context({})
        output = template.render(context)
        output = re.sub(r'\s+', '', output)
        self.assertEqual("<ul>%s</ul>" % "".join("<li>%s" % e for e in [event1, event2]), output.replace("\n", ''))

class EventModelTests(TestCase):

    def test_uses_name_as_string_representation(self):
        event = models.Event(name="An event")
        self.assertEqual(event.name, str(event))

    def test_gets_upcoming_events(self):
        today = datetime.datetime.today()
        event1 = models.Event.objects.create(name="Event1", start_time=today + datetime.timedelta(days=1))
        event2 = models.Event.objects.create(name="Event2", start_time=today + datetime.timedelta(days=2))
        models.Event.objects.create(name="Event3", start_time=today + datetime.timedelta(days=3))

        upcoming_events = models.Event.objects.get_upcoming_events(2)
        self.assertEqual([event1, event2], list(upcoming_events))

    def test_upcoming_events_does_not_return_events_in_the_past(self):
        today = datetime.datetime.today()
        models.Event.objects.create(name="Event1", start_time=today - datetime.timedelta(days=1))
        event2 = models.Event.objects.create(name="Event2", start_time=today + datetime.timedelta(days=1))
        event3 = models.Event.objects.create(name="Event3", start_time=today + datetime.timedelta(days=2))

        upcoming_events = models.Event.objects.get_upcoming_events()
        self.assertEqual([event2, event3], list(upcoming_events))