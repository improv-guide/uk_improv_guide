from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.models.performer import Performer, get_all_performers


def performers(request):
    all_performers: Sequence[Performer] = get_all_performers()
    title = "Performers"
    return render(
        request,
        "performer_index.html",
        {
            "title": title,
            "performers": all_performers,
        },
    )
