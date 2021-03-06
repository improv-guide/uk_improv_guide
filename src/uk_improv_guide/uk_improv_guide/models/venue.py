from typing import List, Sequence

import reversion
from django.db import models
from django_countries.fields import CountryField
from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.lib.site_mappable import SiteMapThing
from uk_improv_guide.lib.slack_notification_mixin import SlackNotificationMixin
from uk_improv_guide.models.city import City
from uk_improv_guide.models.fields.fields import TWITTER_HANDLE
from uk_improv_guide.models.school import School


@reversion.register
class Venue(SlackNotificationMixin, SiteMapThing, AdminableObject, models.Model):
    url_base: str = "venue"

    name = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=256, blank=True)
    website_link = models.CharField(max_length=256, blank=True)
    twitter_handle = TWITTER_HANDLE
    google_maps_link = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, verbose_name="Street Address")
    city = models.CharField(max_length=256, default="London", editable=False)
    postcode = models.CharField(max_length=10, verbose_name="Postal Code")
    email_address = models.CharField(
        max_length=100, verbose_name="Email Address", blank=True
    )
    country = CountryField(blank_label="(select country)", default="GB", editable=False)

    city_obj = models.ForeignKey(
        City,
        on_delete=models.SET_DEFAULT,
        blank=True,
        null=True,
        default=None,
        verbose_name="City",
    )

    school = models.ForeignKey(
        School,
        on_delete=models.SET_DEFAULT,
        blank=True,
        null=True,
        default=None,
        verbose_name="School affiliation",
    )
    image = models.ImageField(upload_to="venue/")

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}, {self.city_obj or 'City not set'}"


def get_all_venues() -> List[Venue]:
    return Venue.objects.all()


def get_venue_by_id(id: int) -> Venue:
    return Venue.objects.get(id=id)


def get_venues_for_city(city_id: int) -> Sequence[Venue]:
    return Venue.objects.filter(city_obj__id=city_id).order_by("name")
