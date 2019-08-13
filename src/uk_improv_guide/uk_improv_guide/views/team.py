from django.shortcuts import render
from pytz import timezone
from uk_improv_guide.models.team import Team, get_team_by_id


def team(request, id: int):
    this_team: Team = get_team_by_id(id)
    title = f"Team: {this_team.name}"
    events = this_team.event_set.all()
    players = this_team.players.all()

    return render(
        request,
        "team.html",
        {
            "title": title,
            "team": this_team,
            "events": events,
            "players": players,
            "og_subject": this_team
        },
    )
