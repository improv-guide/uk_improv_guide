from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.models.resource import Resource, get_all_resources


def resources(request):
    all_podcasts: Sequence[Resource] = get_all_resources().filter(resource_type="P")
    title: str = "Podcasts"
    return render(
        request, "resource_index.html", {"title": title, "resources": all_podcasts}
    )
