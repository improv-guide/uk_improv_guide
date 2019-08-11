from django.shortcuts import render
from uk_improv_guide.models.resource import Resource, get_podcast_by_id
from uk_improv_guide.lib.opengraph import opengraph_website


def resource(request, id: int):
    this_resource: Resource = get_podcast_by_id(id)
    title = f"Podcast: {this_resource.name}"

    return render(
        request,
        "resource.html",
        {
            "title": title,
            "resource": this_resource,
            "og": opengraph_website(title=title, request=request, image=None),
        },
    )
