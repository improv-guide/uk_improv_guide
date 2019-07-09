import logging
from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.performer import Performer
from uk_improv_guide.models.school import School, get_school_by_id
from uk_improv_guide.models.venue import Venue

log = logging.getLogger(__name__)


def school(request, id: int):
    this_school: School = get_school_by_id(id)
    title = this_school.name

    teachers: Sequence[Performer] = this_school.teachers.order_by(
        "family_name", "first_name"
    )
    venues: Sequence[Venue] = this_school.venue_set.order_by("name")

    return render(
        request,
        "school.html",
        {
            "title": title,
            "school": this_school,
            "teachers": teachers,
            "venues": venues,
            "og": opengraph_website(
                title=title, request=request, image=this_school.image
            ),
        },
    )
