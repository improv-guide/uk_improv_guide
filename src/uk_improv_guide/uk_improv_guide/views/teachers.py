from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.models.performer import Performer, get_all_performers


def teachers(request):
    all_performers: Sequence[Performer] = get_all_performers(teachers_only=True)
    title = "Teachers"
    return render(
        request,
        "performer_index.html",
        {
            "title": title,
            "performers": all_performers
        },
    )
