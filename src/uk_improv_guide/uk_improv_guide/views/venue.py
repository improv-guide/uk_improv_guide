from django.http import HttpResponse
from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.venue import Venue, get_all_venues, get_venue_by_id


def venue(request, id: int):
    this_venue: Venue = get_venue_by_id(id)
    title = "Venues"
    return render(
        request,
        "venue.html",
        {
            "title": title,
            "venue": this_venue,
            "og": opengraph_website(
                title=title, url=request.build_absolute_uri(), image=None
            ),
        },
    )
