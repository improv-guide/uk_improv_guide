import uuid

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


@reversion.register
class School(AdminableObject, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="school/", blank=True)
    facebook_link = FACEBOOK_LINK
    instagram_link = INSTAGRAM_LINK
    twitter_handle = TWITTER_HANDLE
    contact_email_address = EMAIL_ADDRESS
    website_link = WEBSITE_LINK

    def __str__(self):
        return self.name
