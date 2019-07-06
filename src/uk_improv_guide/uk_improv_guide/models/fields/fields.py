from django.db import models

TWITTER_HANDLE = models.CharField(
    max_length=100, blank=True, default="", verbose_name="Twitter Link"
)

FACEBOOK_LINK = models.CharField(max_length=256, blank=True)
WEBSITE_LINK = models.CharField(max_length=256, blank=True)
GOOGLE_MAPS_LINK = models.CharField(max_length=256, blank=True)
EMAIL_ADDRESS = models.CharField(
    max_length=100, verbose_name="Email Address", blank=True
)
EVENTBRITE_LINK = models.CharField(max_length=256, blank=True)
INSTAGRAM_LINK = models.CharField(
    max_length=100, blank=True, default="", verbose_name="Instagram Link"
)
IMDB_LINK = models.CharField(
    max_length=100, blank=True, default="", verbose_name="IMDB Link"
)
