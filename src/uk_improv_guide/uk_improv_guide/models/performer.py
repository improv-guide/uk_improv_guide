import logging
import pprint
from typing import Sequence

import reversion
from django.db import models
from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.models.fields.fields import (
    EMAIL_ADDRESS,
    FACEBOOK_LINK,
    INSTAGRAM_LINK,
    TWITTER_HANDLE,
    WEBSITE_LINK,
)

log = logging.getLogger(__name__)


@reversion.register
class Performer(AdminableObject, models.Model):
    first_name = models.CharField(max_length=50, default="")
    middle_names = models.CharField(max_length=60, blank=True, default="")
    family_name = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="performer/", blank=True)
    alias = models.CharField(
        max_length=50, default="", verbose_name="Alias / Performing as", blank=True
    )
    facebook_link = FACEBOOK_LINK
    instagram_link = INSTAGRAM_LINK
    twitter_username = TWITTER_HANDLE
    contact_email_address = EMAIL_ADDRESS
    website_link = WEBSITE_LINK

    imdb_link = models.CharField(
        max_length=100, blank=True, default="", verbose_name="IMDB Link"
    )

    def full_name(self) -> str:
        middle_names: str = self.middle_names or ""
        return " ".join([self.first_name] + middle_names.split() + [self.family_name])

    def name_in_list_order(self):
        middle_names: str = self.middle_names or ""
        return f"{self.family_name}, {self.first_name}"

    def __str__(self) -> str:
        return self.name_in_list_order()


def get_all_performers() -> Sequence[Performer]:
    return Performer.objects.all().order_by("family_name", "first_name")


def get_performer_by_id(id: int) -> Performer:
    p: Performer = Performer.objects.get(id=id)
    pprint.pprint(p)
    return p
