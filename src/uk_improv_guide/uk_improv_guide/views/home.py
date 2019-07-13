import datetime
from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.event import Event, get_events_between_dates
from uk_improv_guide.models.performer import get_featured_performers
from uk_improv_guide.models.team import get_featured_teams


def home(request, hour_gap: int = 48):
    now: datetime.datetime = datetime.datetime.now()
    later: datetime = now + datetime.timedelta(hours=hour_gap)
    events: Sequence[Event] = get_events_between_dates(now, later)
    title: str = "World Improv Guide"
    return render(
        request,
        "home.html",
        {
            "title": "World Improv Guide",
            "hour_gap": hour_gap,
            "events": events,
            "teams": get_featured_teams(),
            "teachers": get_featured_performers(teachers=True),
            "og": opengraph_website(title=title, request=request, image=None),
        },
    )
