import datetime
from typing import Sequence

from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.models.course import Course, get_courses_after_datetime


def courses(request):
    now: datetime.datetime = datetime.datetime.now(tz=timezone("Europe/London"))
    courses: Sequence[Course] = get_courses_after_datetime(now)
    title: str = "Courses"
    return render(
        request,
        "courses_index.html",
        {
            "title": "Improv Courses",
            "courses": courses,
        },
    )
