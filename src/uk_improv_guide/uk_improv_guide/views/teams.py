import datetime
from typing import Sequence

from pytz import timezone

from uk_improv_guide.models.team import Team, get_all_teams

from django.shortcuts import render

def teams(request):
    teams:Sequence[Team] = get_all_teams()
    return render(request, "teams.html", {"title":"Teams", "items":teams})


