from django.shortcuts import render
from uk_improv_guide.models.festival import (
    Festival,
    get_festival_by_id,
    get_festivals_after_datetime,
)
from uk_improv_guide.models.venue import Venue


def festival(request, id: int):
    this_festival: Festival = get_festival_by_id(id)
    title = f"{this_festival.name}"

    return render(
        request,
        "festival.html",
        {
            "title": title,
            "festival": this_festival,
            "teachers": this_festival.teachers.all(),
            "teams": this_festival.teams.all(),
            "teachers": this_festival.teachers.all(),
            "og_subject": this_festival,
        },
    )
