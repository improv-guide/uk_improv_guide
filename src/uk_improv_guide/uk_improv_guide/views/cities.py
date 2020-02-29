from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.models import City
from uk_improv_guide.models.city import get_all_cities


def cities(request):
    cities: Sequence[City] = get_all_cities()
    return render(request, "cities_index.html", {"title": "Cities", "cities": cities})
