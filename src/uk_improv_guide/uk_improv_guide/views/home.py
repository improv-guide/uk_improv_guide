import datetime
import logging
from typing import Sequence

import uk_improv_guide
from django.shortcuts import render
from uk_improv_guide import settings
from uk_improv_guide.models.event import Event, get_events_after_datetime
from uk_improv_guide.models.performer import get_featured_performers
from uk_improv_guide.models.team import get_featured_teams

log = logging.getLogger(__name__)


def home(request, event_days: int = 7):
    events: Sequence[Event] = get_events_after_datetime(dt=datetime.datetime.now())[:10]
    return render(
        request,
        "home.html",
        {
            "title": "Improv Guide",
            "event_days": event_days,
            "events": events,
            "teams": get_featured_teams(),
            "teachers": get_featured_performers(teachers=True),
            "version": uk_improv_guide.__version__,
            "environment": settings.ENIRONMENT_NAME,
        },
    )
