import uuid
from typing import List

import reversion
from django.db import models

from uk_improv_guide.models import School


@reversion.register
class Venue(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=256, blank=True)
    website_link = models.CharField(max_length=256, blank=True)
    google_maps_link = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, verbose_name="Street Address")
    city = models.CharField(max_length=256, default="London")
    postcode = models.CharField(max_length=10, verbose_name="Post Code")
    image = models.ImageField(
        upload_to="static/images/venue/", max_length=100, blank=True
    )
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, to_field="unique_id", verbose_name="School Affiliation")

    def __str__(self) -> str:
        return f"{self.name}, {self.address}"


def get_all_venues() -> List[Venue]:
    return Venue.objects.all()


def get_venue_by_id(id: int) -> Venue:
    return Venue.objects.get(id=id)
