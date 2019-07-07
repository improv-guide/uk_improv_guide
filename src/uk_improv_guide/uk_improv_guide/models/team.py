from typing import Sequence

import reversion
from django.db import models
from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.lib.site_mappable import sitemap_model_object
from uk_improv_guide.models.fields.fields import (
    EMAIL_ADDRESS,
    FACEBOOK_LINK,
    INSTAGRAM_LINK,
    TWITTER_HANDLE,
    WEBSITE_LINK,
)
from uk_improv_guide.models.performer import Performer


@reversion.register
class Team(sitemap_model_object("team"), AdminableObject, models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team/", blank=True)
    facebook_link = FACEBOOK_LINK
    instagram_link = INSTAGRAM_LINK
    twitter_handle = TWITTER_HANDLE
    contact_email_address = EMAIL_ADDRESS
    website_link = WEBSITE_LINK
    players = models.ManyToManyField(
        Performer, verbose_name="Team members", blank=True, related_name="plays_for"
    )

    def __str__(self):
        return self.name


def get_all_teams() -> Sequence[Team]:
    return Team.objects.all().order_by("name")


def get_team_by_id(id: int) -> Team:
    return Team.objects.get(id=id)
