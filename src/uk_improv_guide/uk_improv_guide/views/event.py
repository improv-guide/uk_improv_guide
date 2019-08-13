from django.shortcuts import render
from uk_improv_guide.models.event import (
    Event,
    get_event_by_id,
    get_events_after_datetime,
)
from uk_improv_guide.models.venue import Venue


def event(request, id: int):
    this_event: Event = get_event_by_id(id)
    title = f"{this_event.name}"
    venue: Venue = this_event.venue

    return render(
        request,
        "event.html",
        {
            "title": title,
            "event": this_event,
            "venue": venue,
            "teams": this_event.teams.all(),
            "og_subject": this_event
        },
    )
