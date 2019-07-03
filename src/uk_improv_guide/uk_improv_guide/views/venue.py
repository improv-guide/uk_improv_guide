import logging
from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models import Event
from uk_improv_guide.models.venue import Venue, get_venue_by_id

log = logging.getLogger(__name__)


def venue(request, id: int):
    this_venue: Venue = get_venue_by_id(id)
    title = this_venue.name

    events: Sequence[Event] = this_venue.event_set.order_by("-start_time")

    return render(
        request,
        "venue.html",
        {
            "title": title,
            "venue": this_venue,
            "events": events,
            "og": opengraph_website(
                title=title, request=request, image=this_venue.image
            ),
        },
    )
