import datetime

import pytz
from django.shortcuts import render
from uk_improv_guide.models.team import Team, get_team_by_id


def team(request, id: int):
    now = pytz.utc.localize(datetime.datetime.now())
    this_team: Team = get_team_by_id(id)
    title = f"Team: {this_team.name}"
    events = this_team.event_set.all().order_by("start_time")
    players = this_team.players.all()

    future_events = [e for e in events if e.start_time > now]
    past_events = [e for e in events if e.start_time <= now]

    return render(
        request,
        "team.html",
        {
            "title": title,
            "team": this_team,
            "events": future_events,
            "past_events": past_events,
            "players": players,
            "og_subject": this_team,
        },
    )
