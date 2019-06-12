import datetime
from typing import Sequence

from pytz import timezone

from uk_improv_guide.models.team import Team, get_all_teams

from django.shortcuts import render

def teams(request):
    teams:Sequence[Team] = get_all_teams()
    return render(request, "teams.html", {"title":"Teams", "items":teams})


def team(request, id:int):
    now:datetime.datetime = datetime.datetime.now(tz=timezone("Europe/London"))
    team:Team = Team(id=id)

    events = team.event_set.all()
    players = team.players()

    return render(request, "team.html", {
        "title":"XXXXX",
        "team":team,
        "events":events,
        "players":players
    })