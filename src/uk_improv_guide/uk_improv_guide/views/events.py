import datetime
from typing import Sequence

from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.models.event import Event, get_events_after_datetime


def events(request):
    now: datetime.datetime = datetime.datetime.now(tz=timezone("Europe/London"))
    events: Sequence[Event] = get_events_after_datetime(now)
    title: str = "Events"
    return render(
        request, "events_index.html", {"title": "Improv Guide", "events": events}
    )
