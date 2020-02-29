import logging

from django.shortcuts import render
from uk_improv_guide.models import City
from uk_improv_guide.models.city import get_city_by_id

log = logging.getLogger(__name__)


def city(request, id: int):
    this_city: City = get_city_by_id(id)
    title = this_city.name

    # events: Sequence[Event] = this_city.event_set.order_by("-start_time")

    return render(
        request,
        "city.html",
        {"title": title, "city": this_city, "og_subject": this_city,},
    )
