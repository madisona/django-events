
from django.template.base import Node
from django.template import Library

from events.models import Event

register = Library()

class UpcomingEventsNode(Node):

    def __init__(self, nodelist, events_limit):
        self.nodelist = nodelist
        self.events_limit = events_limit

    def __repr__(self):
        return "<UpcomingEventsNode>"

    def render(self, context):
        context.update(
            dict(upcoming_events=Event.objects.get_upcoming_events(self.events_limit)),
        )
        output = self.nodelist.render(context)
        context.pop()
        return output

@register.tag
def upcoming_events(parser, token):
    """
    Adds upcoming_events as a context variable between the tags.

    For sample::

        {% upcoming_events 5 %}
            {% for event in upcoming_events %}
                {{ event }}
            {% endfor %}
        {% endupcoming_events %}
    """
    bits = token.split_contents()
    nodelist = parser.parse(('endupcoming_events',))
    parser.delete_first_token()
    return UpcomingEventsNode(nodelist, bits[1])