import datetime
from typing import Sequence

import reversion
from django.db import models
from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.lib.site_mappable import SiteMapThing
from uk_improv_guide.lib.sitemaps import register_model_for_site_map
from uk_improv_guide.lib.slack_notification_mixin import SlackNotificationMixin
from uk_improv_guide.models.school import School
from uk_improv_guide.models.performer import Performer
from uk_improv_guide.models.fields.fields import (
    WEBSITE_LINK,
)
from uk_improv_guide.models.venue import Venue


@reversion.register
@register_model_for_site_map
class Course(SlackNotificationMixin, SiteMapThing, AdminableObject, models.Model):
    url_base: str = "course"
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="course/", blank=True)

    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Performer, on_delete=models.SET_NULL, null=True)

    start_time = models.DateTimeField(verbose_name="Show start time")
    lesson_duration = models.FloatField(verbose_name="Lesson duration in hours")
    number_of_lessons = models.IntegerField(verbose_name="Total number of lessons")
    class_show = models.BooleanField(verbose_name="Includes a class show")
    booking_link = WEBSITE_LINK

    class Meta:
        ordering = ["-start_time"]

    def __str__(self):
        return f"{self.school}/{self.name} @ {self.start_time}"

    def get_absolute_url(self) -> str:
        return f"/courses/{self.id}"


def get_courses_after_datetime(dt: datetime.datetime) -> Sequence[Course]:
    return Course.objects.filter(start_time__gte=dt).order_by("start_time")


def get_courses_for_teacher(
    dt: datetime.datetime, performer_id: int
) -> Sequence[Course]:
    return Course.objects.filter(start_time__gte=dt, teacher__id=performer_id).order_by(
        "start_time"
    )


def get_courses_for_school(id: str) -> Sequence[Course]:
    return Course.objects.filter()


def get_course_by_id(id: int) -> Course:
    return Course.objects.get(id=id)
