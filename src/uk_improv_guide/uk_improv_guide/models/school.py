import uuid

import reversion
from django.db import models


@reversion.register
class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="school/", blank=True)
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

    def __str__(self):
        return self.name
