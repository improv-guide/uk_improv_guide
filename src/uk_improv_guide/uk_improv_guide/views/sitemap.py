from django.shortcuts import render
from uk_improv_guide.models.event import get_all_events
from uk_improv_guide.models.performer import get_all_performers
from uk_improv_guide.models.team import get_all_teams


def site_map(request):

    objects = (
        get_all_teams() + get_all_events() + get_all_performers() + get_all_teams()
    )

    return render(request, "sitemap.html", {"objects": objects})
