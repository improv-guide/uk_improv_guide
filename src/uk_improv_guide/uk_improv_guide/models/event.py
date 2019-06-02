from django.db import models

from uk_improv_guide.models.event_series import EventSeries
from uk_improv_guide.models.team import Team
from uk_improv_guide.models.venue import Venue


class Event(models.Model):
    EVENT_TYPES = (
        ('S', 'Show'),
        ('J', 'Jam'),
        ('W', 'Workshop'),
        ('A', 'Audition')
    )

    name = models.CharField(max_length=100, primary_key=True)
    event_type = models.CharField(max_length=1, choices=EVENT_TYPES)
    start_time = models.DateTimeField()
    facebook_link = models.CharField(max_length=256, blank=True)
    eventbrite_link = models.CharField(max_length=256, blank=True)
    venue = models.ForeignKey(
        EventSeries,
        on_delete=models.SET_NULL,
        null=True
    )
    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE
    )
    teams = models.ManyToManyField(Team, verbose_name="teams playing", blank=True)