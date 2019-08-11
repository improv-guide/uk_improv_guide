from django.shortcuts import render
from uk_improv_guide.models.podcast import Podcast, get_podcast_by_id
from uk_improv_guide.lib.opengraph import opengraph_website


def podcast(request, id: int):
    this_podcast: Podcast = get_podcast_by_id(id)
    title = f"Podcast: {this_podcast.name}"

    return render(
        request,
        "podcast.html",
        {
            "title": title,
            "podcast": this_podcast,
            "og": opengraph_website(title=title, request=request, image=None),
        },
    )
