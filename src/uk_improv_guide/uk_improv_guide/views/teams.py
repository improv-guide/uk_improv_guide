from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.team import Team, get_all_teams


def teams(request):
    teams: Sequence[Team] = get_all_teams()
    title: str = "Teams"
    return render(
        request,
        "team_index.html",
        {
            "title": title,
            "items": teams,
            "og": opengraph_website(
                title=title, request=request, image=None
            ),
        },
    )
