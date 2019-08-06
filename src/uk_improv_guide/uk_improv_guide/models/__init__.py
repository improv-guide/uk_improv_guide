from typing import Set

from django.db import models

from uk_improv_guide.models.festival import Festival
from .course import Course
from .event import Event
from .event_series import EventSeries
from .performer import Performer
from .school import School
from .signals import create_user_profile
from .team import Team
from .venue import Venue

ALL_MODELS: Set[models.Model] = {
    Event,
    Performer,
    Team,
    Venue,
    EventSeries,
    School,
    Course,
    Festival,
}
