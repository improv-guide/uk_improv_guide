import datetime
from datetime import timezone
from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.models import Team

from uk_improv_guide.models.performer import Performer, get_all_performers, get_performer_by_id

def performers(request):
    performers:Sequence[Performer] = get_all_performers()
    return render(request, "performer.html", {"title":"Performers", "items":performers})


def performer(request, id:int):
    this_performer:Performer = get_performer_by_id(id)
    teams:Sequence[Team] = []

    return render(request, "performer.html", {
        "title": f"{this_performer.full_name()}",
        "performer":this_performer,
        "teams":teams,
    })