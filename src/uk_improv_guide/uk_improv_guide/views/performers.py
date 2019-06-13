import datetime
from datetime import timezone
from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.uk_improv_guide.models import Team

from uk_improv_guide.models import Performer, get_all_performers, get_performer


def performers(request):
    performers:Sequence[Performer] = get_all_performers()
    return render(request, "performers.html", {"title":"Performers", "items":performers})


def performer(request, id:int):
    now:datetime.datetime = datetime.datetime.now(tz=timezone("Europe/London"))

    performer:Performer = get_performer(id)
    teams:Sequence[Team] = performer.plays_for_set()

    return render(request, "performer.html", {
        "title":f"{performer.first_name} {performer.family_name}",
        "performer":performer,
        "teams":teams,
    })