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


@reversion.register
class Podcast(SlackNotificationMixin, SiteMapThing, AdminableObject, models.Model):
    url_base: str = "podcast"
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team/", blank=True)
    facebook_link = FACEBOOK_LINK
    instagram_link = INSTAGRAM_LINK
    twitter_handle = TWITTER_HANDLE
    rss_feed_link = RSS_FEED_LINK
    contact_email_address = EMAIL_ADDRESS
    website_link = WEBSITE_LINK
    hosts = models.ManyToManyField(
        Performer, verbose_name="Team members", blank=True, related_name="plays_for"
    )

    @staticmethod
    def model_admin():
        return PodcastAdmin

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return f"/podcasts/{self.id}"


class PodcastAdminForm(ModelForm):
    excludes = []

    class Meta:
        model = Podcast
        fields = "__all__"
        widgets = {"players": FilteredSelectMultiple("Team members", False)}


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
def get_all_podcasts() -> Sequence[Podcast]:
    return Podcast.objects.all().order_by("name")


#
#
# def get_team_by_id(id: int) -> Team:
#     return Team.objects.get(id=id)
