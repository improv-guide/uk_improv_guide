from django.shortcuts import render
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.event import get_events_by_venue_id
from uk_improv_guide.models.venue import Venue, get_all_venues, get_venue_by_id


def venue(request, id: int):
    this_venue: Venue = get_venue_by_id(id)
    title = this_venue.name
    events = get_events_by_venue_id(this_venue.id)

    return render(
        request,
        "venue.html",
        {
            "title": title,
            "venue": this_venue,
            "events": events,
            "og": opengraph_website(
                title=title, url=request.build_absolute_uri(), image=this_venue.image
            ),
        },
    )
