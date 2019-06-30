from typing import Set

from django.db import models

from .event import Event
from .event_series import EventSeries
from .performer import Performer
from .school import School
from .team import Team
from .venue import Venue

ALL_MODELS: Set[models.Model] = {Event, Performer, Team, Venue, EventSeries, School}
