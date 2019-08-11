import datetime
import logging
from typing import Sequence

from django.http import HttpResponse
from django.urls import reverse
from ics import Calendar
from ics import Event as ICSEvent
from uk_improv_guide.models.event import Event
from uk_improv_guide.models.team import Team, get_team_by_id

log = logging.getLogger(__name__)


def team_event_calendar(request, id: int):
    team: Team = get_team_by_id(id)
    title = f"Team calendar: {team.name}"

    events: Sequence[Event] = list(team.event_set.all())

    log.warning(f"All events: {events}")

    c = Calendar()

    for event in events:
        duration: datetime.timedelta = datetime.timedelta(
            seconds=event.duration * 60 * 60
        )

        location: str = f"{event.venue.name}, {event.venue.address}, {event.venue.city}, {event.venue.postcode}, {event.venue.country.name}"
        url: str = request.build_absolute_uri(reverse("event", kwargs={"id": event.id}))
        description: str = f"{team.name} will be performing in {event.name} @ {event.venue.name}"

        e: ICSEvent = ICSEvent(
            name=event.name,
            duration=duration,
            description=description,
            location=location,
            url=url,
            transparent=False,
        )

        c.events.add(e)
    c.events

    content: str = "".join(c)

    return HttpResponse(content, "text/calendar", 200)
