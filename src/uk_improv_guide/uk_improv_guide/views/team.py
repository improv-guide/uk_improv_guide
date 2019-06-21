import datetime
from pytz import timezone
from uk_improv_guide.models.team import Team, get_team_by_id
from django.shortcuts import render

def team(request, id:int):
    now:datetime.datetime = datetime.datetime.now(tz=timezone("Europe/London"))
    team:Team = get_team_by_id(id)

    events = team.event_set.all()
    players = team.players.all()

    return render(request, "team.html", {
        "title":"XXXXX",
        "team":team,
        "events":events,
        "players":players
    })