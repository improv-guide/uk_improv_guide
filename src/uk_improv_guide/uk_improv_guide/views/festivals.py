import datetime
from typing import Sequence

from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.festival import Festival, get_festivals_after_datetime


def festivals(request):
    now: datetime.datetime = datetime.datetime.now(tz=timezone("Europe/London"))
    festivals: Sequence[Festival] = get_festivals_after_datetime(now)
    title: str = "Festivals"
    return render(
        request,
        "festivals_index.html",
        {
            "title": "Improv Festivals",
            "festivals": festivals,
            "og": opengraph_website(title=title, request=request, image=None),
        },
    )
