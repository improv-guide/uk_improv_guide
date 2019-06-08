import datetime
from typing import Sequence

from pytz import timezone

from uk_improv_guide.models.team import Team, get_all_teams

from django.shortcuts import render


def teams(request):
    now:datetime.datetime = datetime.datetime.now(tz=timezone("Europe/London"))
    teams:Sequence[Team] = get_all_teams()
    return render(request, "teams.html", {"title":"Teams", "items":teams})


def team(request, id:int):
    team = Team(id=id)
    events = []
    players = []
    return render(request, "team.html", {"title":"Teams", "team":team, "events":events, "players":players})