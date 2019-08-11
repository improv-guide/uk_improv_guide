from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.lib.opengraph import opengraph_website
from uk_improv_guide.models.podcast import Podcast, get_all_podcasts


def podcasts(request):
    podcasts: Sequence[Podcast] = get_all_podcasts()
    title: str = "Podcasts"
    return render(
        request,
        "podcast_index.html",
        {
            "title": title,
            "podcasts": podcasts,
            "og": opengraph_website(title=title, request=request, image=None),
        },
    )
