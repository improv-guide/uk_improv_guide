import logging
import pprint
from typing import Sequence

import reversion
from django.db import models

log = logging.getLogger(__name__)


@reversion.register
class Performer(models.Model):
    first_name = models.CharField(max_length=50, default="")
    middle_names = models.CharField(max_length=60, blank=True, default="")
    family_name = models.CharField(max_length=50, default="")
    alias = models.CharField(
        max_length=50, default="", verbose_name="Alias / Performing as", blank=True
    )
    facebook_link = models.CharField(
        max_length=100, blank=True, default="", verbose_name="Facebook Link"
    )
    instagram_link = models.CharField(
        max_length=100, blank=True, default="", verbose_name="Instagram Link"
    )
    twitter_link = models.CharField(
        max_length=100, blank=True, default="", verbose_name="Twitter Link"
    )
    imdb_link = models.CharField(
        max_length=100, blank=True, default="", verbose_name="IMDB Link"
    )
    contact_email_address = models.CharField(max_length=100, blank=True, default="")

    def full_name(self) -> str:
        middle_names: str = self.middle_names or ""
        return " ".join([self.first_name] + middle_names.split() + [self.family_name])

    def __str__(self) -> str:
        return self.full_name()


def get_all_performers() -> Sequence[Performer]:
    return Performer.objects.all().order_by('family_name', 'first_name')


def get_performer_by_id(id: int) -> Performer:
    p: Performer = Performer.objects.get(id=id)
    pprint.pprint(p)
    return p
