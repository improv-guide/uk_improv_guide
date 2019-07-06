import datetime
import logging
from typing import Sequence

from django.shortcuts import render
from uk_improv_guide.lib.opengraph import opengraph_person, opengraph_website
from uk_improv_guide.models import Event, Team
from uk_improv_guide.models.event import get_events_after_datetime_for_performer_id
from uk_improv_guide.models.performer import Performer, get_performer_by_id

log = logging.getLogger(__name__)


def performer(request, id: int):
    now = datetime.datetime.now()
    this_performer: Performer = get_performer_by_id(id)

    teams: Sequence[Team] = this_performer.plays_for.all

    events: Sequence[Event] = get_events_after_datetime_for_performer_id(
        now, this_performer.id
    )

    title = f"{this_performer.full_name()}"

    return render(
        request,
        "performer.html",
        {
            "title": title,
            "performer": this_performer,
            "teams": teams,
            "events": events,
            "og": opengraph_person(
                title=title,
                first_name=this_performer.first_name,
                family_name=this_performer.family_name,
                image=this_performer.image,
                request=request,
            ),
        },
    )
