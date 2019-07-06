import re

from django.core.exceptions import ValidationError
from django.db import models


def validate_twitter_handle(value: str):
    if not re.match("^@?(\w){1,15}$", value):
        raise ValidationError(
            "Twitter usernames should begin with an @ and be no more than 15 chars long."
        )


TWITTER_HANDLE = models.CharField(
    max_length=100,
    blank=True,
    default="",
    verbose_name="Twitter username",
    validators=[validate_twitter_handle],
)

FACEBOOK_LINK = models.URLField(max_length=256, blank=True)
WEBSITE_LINK = models.URLField(max_length=256, blank=True)
GOOGLE_MAPS_LINK = models.URLField(max_length=256, blank=True)
EMAIL_ADDRESS = models.EmailField(
    max_length=100, verbose_name="Email Address", blank=True
)
EVENTBRITE_LINK = models.URLField(max_length=256, blank=True)
INSTAGRAM_LINK = models.URLField(
    max_length=100, blank=True, default="", verbose_name="Instagram Link"
)
IMDB_LINK = models.URLField(
    max_length=100, blank=True, default="", verbose_name="IMDB Link"
)
