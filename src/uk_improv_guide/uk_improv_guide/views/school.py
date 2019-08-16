import datetime
import logging
from typing import Sequence

from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.models.course import Course
from uk_improv_guide.models.performer import Performer
from uk_improv_guide.models.school import School, get_school_by_id
from uk_improv_guide.models.venue import Venue

log = logging.getLogger(__name__)


def school(request, id: int):
    now: datetime.datetime = datetime.datetime.now(tz=timezone("Europe/London"))
    this_school: School = get_school_by_id(id)
    title = this_school.name

    teachers: Sequence[Performer] = this_school.teachers.order_by(
        "family_name", "first_name"
    )

    courses: Sequence[Course] = this_school.courses.filter(start_time__gt=now)
    log.warning(f"Courses: {courses}")
    venues: Sequence[Venue] = this_school.venue_set.order_by("name")

    return render(
        request,
        "school.html",
        {
            "title": title,
            "school": this_school,
            "teachers": teachers,
            "venues": venues,
            "courses": courses,
            "og_subject": this_school,
        },
    )
