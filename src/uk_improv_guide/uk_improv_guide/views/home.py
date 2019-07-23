import datetime
from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.event import Event, get_events_between_dates
from uk_improv_guide.models.performer import get_featured_performers
from uk_improv_guide.models.team import get_featured_teams


def home(request, event_days: int = 7):
    now: datetime.datetime = datetime.datetime.now()
    later: datetime = now + datetime.timedelta(hours=24 * event_days)
    events: Sequence[Event] = get_events_between_dates(now, later)
    title: str = "Improv Guide"
    return render(
        request,
        "home.html",
        {
            "title": "World Improv Guide",
            "event_days": event_days,
            "events": events,
            "teams": get_featured_teams(),
            "teachers": get_featured_performers(teachers=True),
            "og": opengraph_website(title=title, request=request, image=None),
        },
    )
