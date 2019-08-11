from typing import Sequence

import reversion
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models
from django.forms import ModelForm
from reversion.admin import VersionAdmin
from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.lib.site_mappable import SiteMapThing
from uk_improv_guide.lib.slack_notification_mixin import SlackNotificationMixin
from uk_improv_guide.models.fields.fields import (
    EMAIL_ADDRESS,
    FACEBOOK_LINK,
    INSTAGRAM_LINK,
    RSS_FEED_LINK,
    TWITTER_HANDLE,
    WEBSITE_LINK,
)
from uk_improv_guide.models.performer import Performer

RESOURCE_TYPES = {
    "B": "Blog",
    "P": "Podcast",
    "R": "Reference"
}

@reversion.register
class Resource(SlackNotificationMixin, SiteMapThing, AdminableObject, models.Model):
    url_base: str = "resource"
    name = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=1, choices=[a for a in RESOURCE_TYPES.items()])
    image = models.ImageField(upload_to="team/", blank=True)
    rss_feed_link = RSS_FEED_LINK
    website_link = WEBSITE_LINK
    contributors = models.ManyToManyField(
        Performer, verbose_name="Team members", blank=True, related_name="hosts_podcasts"
    )

    @staticmethod
    def model_admin():
        return PodcastAdmin

    class Meta:
        verbose_name="Blog/Podcast"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return f"/resources/{self.id}"


class PodcastAdminForm(ModelForm):
    excludes = []

    class Meta:
        model = Resource
        fields = "__all__"
        widgets = {"contributors": FilteredSelectMultiple("Team members", False)}


class PodcastAdmin(VersionAdmin):
    form = PodcastAdminForm
    save_as = True
    search_fields = ["name"]
    view_on_site = True


#
#
# def get_featured_teams(order: str = "?", limit: int = 5) -> Sequence[Performer]:
#     teams = Team.objects.exclude(image="")
#     return teams.order_by(order)[:limit]
#
#
def get_all_resources() -> Sequence[Resource]:
    return Resource.objects.all().order_by("name")

def get_podcast_by_id(id: int) -> Resource:
    return Resource.objects.get(id=id)
