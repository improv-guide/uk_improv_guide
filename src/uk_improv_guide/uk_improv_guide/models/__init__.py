from typing import Set

from django.db import models

from .event import Event
from .performer import Performer
from .team import Team
from .venue import Venue
from .event_series import EventSeries
from .school import School

ALL_MODELS: Set[models.Model] = {Event, Performer, Team, Venue, EventSeries, School}
