from typing import Sequence

import reversion
from django.db import models
from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.models.performer import Performer


@reversion.register
class Team(AdminableObject, models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team/", blank=True)
    facebook_link = models.CharField(
        max_length=100, blank=True, default="", verbose_name="Facebook Link"
    )
    instagram_link = models.CharField(
        max_length=100, blank=True, default="", verbose_name="Instagram Link"
    )
    twitter_link = models.CharField(
        max_length=100, blank=True, default="", verbose_name="Twitter Link"
    )
    contact_email_address = models.CharField(max_length=100, blank=True, default="")
    website_link = models.CharField(max_length=256, blank=True)
    players = models.ManyToManyField(
        Performer, verbose_name="Team members", blank=True, related_name="plays_for"
    )

    def __str__(self):
        return self.name


def get_all_teams() -> Sequence[Team]:
    return Team.objects.all().order_by("name")


def get_team_by_id(id: int) -> Team:
    return Team.objects.get(id=id)
