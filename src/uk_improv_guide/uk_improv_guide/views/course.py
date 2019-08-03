from django.shortcuts import render
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.course import Course, get_course_by_id
from uk_improv_guide.models.venue import Venue


def course(request, id: int):
    this_course: Course = get_course_by_id(id)
    title = f"{this_course.school.name} / {this_course.name}"
    venue: Venue = this_course.venue

    return render(
        request,
        "course.html",
        {
            "title": title,
            "course": this_course,
            "venue": venue,
            "og": opengraph_website(
                title=title, request=request, image=this_course.image
            ),
        },
    )
