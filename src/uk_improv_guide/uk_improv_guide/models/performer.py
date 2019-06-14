import pprint
from typing import Sequence, List

from django.db import models
import reversion
import logging

log = logging.getLogger(__name__)


@reversion.register
class Performer(models.Model):
    first_name = models.CharField(max_length=50, default="")
    middle_names = models.CharField(max_length=60, blank=True, default="")
    family_name = models.CharField(max_length=50, default="")
    alias = models.CharField(max_length=50, default="", verbose_name="Alias / Performing as", blank=True)
    facebook_link = models.CharField(max_length=100, blank=True, default="", verbose_name="Facebook Link")
    twitter_link = models.CharField(max_length=100, blank=True, default="", verbose_name="Twitter Link")
    imdb_link = models.CharField(max_length=100, blank=True, default="", verbose_name="IMDB Link")
    contact_email_address = models.CharField(max_length=100, blank=True, default="")

    def __str__(self)->str:
        return "%s %s" % (self.first_name, self.family_name)



def get_all_performers()->Sequence[Performer]:
    return Performer.objects.all()


def get_performer_by_id(id:int)->Performer:
    p:Performer = Performer(id=id)
    print("XXXXXXX")
    log.warning("YYYYY")
    pprint.pprint(p)
    return p

