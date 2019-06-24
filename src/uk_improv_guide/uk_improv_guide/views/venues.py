from typing import Sequence

from django.http import HttpResponse
from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.models.venue import Venue, get_all_venues


def venues(request):
    venues: Sequence[Venue] = get_all_venues()
    return render(request, "venues.html", {"title": "Venues", "venues": venues})
