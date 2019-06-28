import uuid
from typing import Sequence

import reversion
from django.db import models

from uk_improv_guide.models.school import School
from uk_improv_guide.models.performer import Performer


@reversion.register
class Team(models.Model):
    # unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=100, blank=True, default="")
    contact_email_address = models.CharField(max_length=100, blank=True, default="")
    players = models.ManyToManyField(
        Performer, verbose_name="Team members", blank=True, related_name="plays_for"
    )
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, to_field="unique_id", verbose_name="School Affiliation")

    def __str__(self):
        return self.name


def get_all_teams() -> Sequence[Team]:
    return Team.objects.all()


def get_team_by_id(id: int) -> Team:
    return Team.objects.get(id=id)
