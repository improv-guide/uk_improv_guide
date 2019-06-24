from typing import Set

from django.db import models

from .event import Event
from .performer import Performer
from .team import Team
from .venue import Venue

ALL_MODELS: Set[models.Model] = {Event, Performer, Team, Venue}
