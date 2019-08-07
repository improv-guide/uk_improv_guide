from typing import Set

from django.db import models

from uk_improv_guide.models.festival import Festival
from uk_improv_guide.models.course import Course
from uk_improv_guide.models.event import Event
from uk_improv_guide.models.event_series import EventSeries
from uk_improv_guide.models.performer import Performer
from uk_improv_guide.models.school import School
from uk_improv_guide.models.signals import create_user_profile
from uk_improv_guide.models.team import Team
from uk_improv_guide.models.venue import Venue

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
