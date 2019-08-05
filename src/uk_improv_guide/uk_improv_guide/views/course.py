import datetime
from typing import Optional

from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.course import Course, get_course_by_id
from uk_improv_guide.models.venue import Venue


def days_until_start(course: Course, now: Optional[datetime.datetime] = None) -> int:
    now = now or datetime.datetime.now(tz=timezone("Europe/London"))
    td: datetime.timedelta = course.start_time - now
    return td.days


def course(request, id: int):
    this_course: Course = get_course_by_id(id)
    title = f"{this_course.school.name} / {this_course.name}"
    venue: Venue = this_course.venue

    _days_until_start: int = days_until_start(this_course)

    return render(
        request,
        "course.html",
        {
            "title": title,
            "course": this_course,
            "has_started": _days_until_start < 0,
            "days_until_start": _days_until_start,
            "venue": venue,
            "og": opengraph_website(
                title=title, request=request, image=this_course.image
            ),
        },
    )
