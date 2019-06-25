from django.http import HttpResponse
from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.models.venue import Venue, get_all_venues, get_venue_by_id


def venue(request, id: int):
    this_venue: Venue = get_venue_by_id(id)
    return render(request, "venue.html", {"title": "Venues", "venue": this_venue})
