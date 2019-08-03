import datetime
from typing import Sequence

from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.event import Event, get_events_after_datetime


def courses(request):
    now: datetime.datetime = datetime.datetime.now(tz=timezone("Europe/London"))
    events: Sequence[Event] = get_events_after_datetime(now)
    title: str = "Courses"
    return render(
        request,
        "courses_index.html",
        {
            "title": "Improv Courses",
            "events": events,
            "og": opengraph_website(title=title, request=request, image=None),
        },
    )
