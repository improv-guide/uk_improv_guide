import uuid
from typing import List

import reversion
from django.db import models
from django_countries.fields import CountryField

from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.lib.site_mappable import SiteMapThing
from uk_improv_guide.lib.slack_notification_mixin import SlackNotificationMixin
from uk_improv_guide.models.fields.fields import (
    EMAIL_ADDRESS,
    FACEBOOK_LINK,
    INSTAGRAM_LINK,
    TWITTER_HANDLE,
    WEBSITE_LINK,
)


@reversion.register
class School(SlackNotificationMixin, SiteMapThing, AdminableObject, models.Model):
    url_base: str = "school"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="school/", blank=True)
    facebook_link = FACEBOOK_LINK
    instagram_link = INSTAGRAM_LINK
    twitter_handle = TWITTER_HANDLE
    contact_email_address = EMAIL_ADDRESS
    website_link = WEBSITE_LINK
    country = CountryField(blank_label="(select country)", default="GB")



    def __str__(self):
        return self.name


def get_school_by_id(id:int)->School:
    return School.objects.get(id=id)

def get_all_schools() -> List[School]:
    return School.objects.all()