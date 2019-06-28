import datetime
import uuid
from typing import Sequence

import reversion
from django.db import models
from uk_improv_guide.models.event_series import EventSeries
from uk_improv_guide.models.team import Team
from uk_improv_guide.models.venue import Venue


@reversion.register
class Event(models.Model):
    EVENT_TYPES = (("S", "Show"), ("J", "Jam"), ("W", "Workshop"), ("A", "Audition"))

    # unique_id = models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=1, choices=EVENT_TYPES)
    start_time = models.DateTimeField(verbose_name="Show start time")
    facebook_link = models.CharField(max_length=256, blank=True)
    eventbrite_link = models.CharField(max_length=256, blank=True)
    event_series = models.ForeignKey(EventSeries, on_delete=models.SET_NULL, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    series = models.ForeignKey(EventSeries, on_delete=models.SET_NULL, null=True, related_name="xxxxx")
    teams = models.ManyToManyField(Team, verbose_name="teams playing", blank=True)

    def __str__(self):
        return f"{self.name} - @ {self.start_time} - {self.venue.name}"


def get_events_after_datetime(dt: datetime.datetime) -> Sequence[Event]:
    return Event.objects.filter(start_time__gte=dt).order_by("start_time")


def get_events_after_datetime_for_performer_id(
    dt: datetime.datetime, performer_id: int
) -> Sequence[Event]:
    return Event.objects.filter(
        start_time__gte=dt, teams__players__id=performer_id
    ).order_by("start_time")
