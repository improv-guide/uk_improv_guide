from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.models.team import Team, get_all_teams


def teams(request):
    teams: Sequence[Team] = get_all_teams()
    return render(request, "team_index.html", {"title": "Teams", "items": teams})
