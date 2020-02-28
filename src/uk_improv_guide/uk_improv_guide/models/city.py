from typing import List

import reversion
from django.db import models
from django_countries.fields import CountryField
from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.lib.site_mappable import SiteMapThing
from uk_improv_guide.lib.slack_notification_mixin import SlackNotificationMixin


@reversion.register
class City(SlackNotificationMixin, SiteMapThing, AdminableObject, models.Model):
    name = models.CharField(max_length=100)
    country = CountryField(blank_label="(select country)", default="GB")
    image =  models.ImageField(upload_to="city/", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Cities"

    def __str__(self) -> str:
        return f"{self.name}, {self.country}"


def get_all_cities() -> List[City]:
    return City.objects.all()


def get_venue_by_id(id: int) -> City:
    return City.objects.get(id=id)
