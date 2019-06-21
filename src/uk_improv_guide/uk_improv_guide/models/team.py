from typing import Sequence

from django.db import models

from uk_improv_guide.models.performer import Performer
import reversion


@reversion.register
class Team(models.Model):
    name = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=100, blank=True, default="")
    contact_email_address = models.CharField(max_length=100, blank=True, default="")
    players = models.ManyToManyField(
        Performer,
        verbose_name="Team members",
        blank=True,
        related_name="plays_for"
    )

    def __str__(self):
        return self.name


def get_all_teams()->Sequence[Team]:
    return Team.objects.all()


def get_team_by_id(id:int)->Team:
    return Team.objects.get(id=id)