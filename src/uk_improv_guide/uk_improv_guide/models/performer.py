import logging
import pprint
from typing import Sequence

import reversion
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models
from django.forms import ModelForm, forms
from reversion.admin import VersionAdmin
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
from uk_improv_guide.models.school import School

log = logging.getLogger(__name__)


@reversion.register
class Performer(SlackNotificationMixin, SiteMapThing, AdminableObject, models.Model):
    url_base: str = "performer"

    first_name = models.CharField(max_length=50, default="")
    middle_names = models.CharField(max_length=60, blank=True, default="")
    family_name = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="performer/", blank=True)
    alias = models.CharField(
        max_length=50, default="", verbose_name="Alias / Performing as", blank=True
    )

    facebook_link = FACEBOOK_LINK
    instagram_link = INSTAGRAM_LINK
    twitter_handle = TWITTER_HANDLE
    contact_email_address = EMAIL_ADDRESS
    website_link = WEBSITE_LINK

    imdb_link = models.CharField(
        max_length=100, blank=True, default="", verbose_name="IMDB Link"
    )

    teaches_for = models.ManyToManyField(
        School,
        verbose_name="Teaches at this school",
        blank=True,
        related_name="teachers",
    )

    @staticmethod
    def model_admin():
        return PerformerAdmin

    class Meta:
        ordering = ["family_name", "first_name"]

    def full_name(self) -> str:
        middle_names: str = self.middle_names or ""
        return " ".join([self.first_name] + middle_names.split() + [self.family_name])

    def middle_initials(self):
        return [n[0] for n in self.middle_names.split(" ") if n]

    def name_in_list_order(self):
        if self.middle_names:
            initials = " ".join(self.middle_initials())
            return f"{self.family_name}, {self.first_name} {initials}"
        return f"{self.family_name}, {self.first_name}"

    def get_absolute_url(self):
        return "/performers/%i" % self.id

    def __str__(self) -> str:
        return self.name_in_list_order()


class PerformerAdminForm(ModelForm):
    excludes = []

    class Meta:
        model = Performer
        fields = "__all__"
        widgets = {"teaches_for": FilteredSelectMultiple("Teaches For", False)}


class PerformerAdmin(VersionAdmin):
    form = PerformerAdminForm
    fields = (
        ("first_name", "middle_names", "family_name"),
        "alias",
        "image",
        "teaches_for",
        "facebook_link",
        "instagram_link",
        "twitter_handle",
        "contact_email_address",
        "website_link",
        "imdb_link",
    )
    save_as = True
    search_fields = ["first_name", "family_name"]
    view_on_site = True


def get_all_performers(teachers_only=False) -> Sequence[Performer]:
    performers = Performer.objects.all().order_by("family_name", "first_name")

    if teachers_only:
        performers = performers.exclude(teaches_for=None)

    return performers


def get_featured_performers(
    teachers=False, order: str = "?", limit: int = 5
) -> Sequence[Performer]:
    performers = Performer.objects.exclude(image="")

    if teachers:
        performers = performers.exclude(teaches_for=None)

    return performers.order_by(order)[:limit]


def get_performer_by_id(id: int) -> Performer:
    p: Performer = Performer.objects.get(id=id)
    pprint.pprint(p)
    return p
