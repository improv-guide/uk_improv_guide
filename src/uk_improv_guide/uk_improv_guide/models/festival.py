import datetime
import logging
from typing import Sequence

import reversion
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models
from django.forms import ModelForm
from reversion.admin import VersionAdmin
from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.lib.site_mappable import SiteMapThing
from uk_improv_guide.lib.sitemaps import register_model_for_site_map
from uk_improv_guide.lib.slack_notification_mixin import SlackNotificationMixin
from uk_improv_guide.models.fields.fields import (
    DESCRIPTION,
    EVENTBRITE_LINK,
    FACEBOOK_LINK,
    WEBSITE_LINK,
)
from uk_improv_guide.models.performer import Performer
from uk_improv_guide.models.school import School
from uk_improv_guide.models.team import Team
from uk_improv_guide.models.utils import link_model_form_and_admin
from uk_improv_guide.models.venue import Venue

log = logging.getLogger(__name__)


@reversion.register
@register_model_for_site_map
class Festival(SlackNotificationMixin, SiteMapThing, AdminableObject, models.Model):
    url_base: str = "event"

    FESTIVAL_TYPES = (("F", "Festival"), ("R", "Retreat"))
    name = models.CharField(max_length=100)
    long_description = (DESCRIPTION,)
    image = models.ImageField(upload_to="event/", blank=True)
    festival_type = models.CharField(max_length=1, choices=FESTIVAL_TYPES)
    start_time = models.DateTimeField(verbose_name="Festival start time")
    end_time = models.DateTimeField(verbose_name="Festival end time")
    facebook_link = FACEBOOK_LINK
    eventbrite_link = EVENTBRITE_LINK
    website_link = WEBSITE_LINK
    venues = models.ManyToManyField(Venue, blank=True)
    teams = models.ManyToManyField(Team, verbose_name="teams playing", blank=True)
    teachers = models.ManyToManyField(
        Performer, verbose_name="teachers teaching", blank=True
    )
    school = models.ForeignKey(School, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ["-start_time"]

    def __str__(self):
        return f"{self.name} - @ {self.start_time} - {self.venue.name}"

    def get_absolute_url(self) -> str:
        return f"/festivals/{self.id}"


class FestivalAdminForm(ModelForm):
    excludes = []

    class Meta:
        fields = "__all__"
        widgets = {
            "teams": FilteredSelectMultiple("Teams", False),
            "teachers": FilteredSelectMultiple("Teachers", False),
            "venues": FilteredSelectMultiple("Venues", False),
        }


class FestivalAdmin(VersionAdmin):
    save_as = True
    search_fields = ["name"]
    view_on_site = True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teachers":
            log.warning("XXXX TEACHERS!")
            kwargs["queryset"] = Performer.objects.exclude(teaches_for=None)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


def get_festivals_after_datetime(dt: datetime.datetime) -> Sequence[Festival]:
    return Festival.objects.filter(start_time__gte=dt).order_by("start_time")


def get_all_festivals() -> Sequence[Festival]:
    return Festival.objects.all()


def get_festival_by_id(id: int) -> Festival:
    f: Festival = Festival.objects.get(id=id)
    return f


link_model_form_and_admin(model=Festival, form=FestivalAdminForm, admin=FestivalAdmin)
