from django.shortcuts import render
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.festival import (
    Festival,
    get_festival_by_id,
    get_festivals_after_datetime,
)
from uk_improv_guide.models.venue import Venue


def festival(request, id: int):
    this_festival: Festival = get_festival_by_id(id)
    title = f"{this_festival.name}"
    venue: Venue = this_festival.venue

    return render(
        request,
        "festival.html",
        {
            "title": title,
            "festival": this_festival,
            "teachers": this_festival.teachers.all(),
            "venue": venue,
            "teams": this_festival.teams.all(),
            "teachers": this_festival.teachers.all(),
            "og": opengraph_website(
                title=title, request=request, image=this_festival.image
            ),
        },
    )
