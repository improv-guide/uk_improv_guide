import logging
from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.models import City, Venue
from uk_improv_guide.models.city import get_city_by_id
from uk_improv_guide.models.event import Event, get_events_for_city
from uk_improv_guide.models.venue import get_venues_for_city

log = logging.getLogger(__name__)


def city(request, city_id: int):
    this_city: City = get_city_by_id(city_id)
    title = this_city.name
    events: Sequence[Event] = get_events_for_city(city_id=city_id)
    venues: Sequence[Venue] = get_venues_for_city(city_id=city_id)

    return render(
        request,
        "city.html",
        {"title": title, "city": this_city, "og_subject": this_city, "events": events, "venues": venues},
    )
