from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.models.event import Event, get_events_after_datetime


def event(request, id: int):
    this_event: Event = get_event_by_id(id)

    return render(
        request,
        "event.html",
        {
            "title": f"{this_event.name}",
            "performer": this_performer,
            "teams": teams,
            "events": events,
        },
    )
