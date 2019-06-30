from typing import List

import reversion
from django.db import models
from django_countries.fields import CountryField
from uk_improv_guide.models.school import School


@reversion.register
class Venue(models.Model):
    name = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=256, blank=True)
    website_link = models.CharField(max_length=256, blank=True)
    google_maps_link = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, verbose_name="Street Address")
    city = models.CharField(max_length=256, default="London")
    postcode = models.CharField(max_length=10, verbose_name="Postal Code")
    country = CountryField(blank_label="(select country)", default="GB")
    school = models.ForeignKey(
        School,
        on_delete=models.SET_DEFAULT,
        blank=True,
        null=True,
        default=None,
        verbose_name="School affiliation",
    )
    image = models.ImageField(upload_to="venue/", blank=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.city}, {self.country}"


def get_all_venues() -> List[Venue]:
    return Venue.objects.all()


def get_venue_by_id(id: int) -> Venue:
    return Venue.objects.get(id=id)
