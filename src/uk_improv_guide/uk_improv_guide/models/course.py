import datetime
from typing import Sequence

import reversion
from django import forms
from django.db import models
from reversion.admin import VersionAdmin
from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.lib.site_mappable import SiteMapThing
from uk_improv_guide.lib.sitemaps import register_model_for_site_map
from uk_improv_guide.lib.slack_notification_mixin import SlackNotificationMixin
from uk_improv_guide.models.fields.fields import WEBSITE_LINK
from uk_improv_guide.models.performer import Performer
from uk_improv_guide.models.school import School
from uk_improv_guide.models.venue import Venue


class CourseAdmin(VersionAdmin):
    save_as = True

    search_fields = ["name"]
    view_on_site = True

    fields = (
        ("school", "name"),
        "image",
        "course_link",
        "start_time",
        "lesson_duration",
        "number_of_lessons",
        "venue",
        "teacher",
        "class_show",
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = Performer.objects.exclude(teaches_for=None)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@reversion.register
@register_model_for_site_map
class Course(SlackNotificationMixin, SiteMapThing, AdminableObject, models.Model):
    url_base: str = "courses"
    name = models.CharField(max_length=100, help_text="The name of your course, but without the school name or any branding.",)
    image = models.ImageField(upload_to="course/", blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, help_text="Where will this clas be taught?",)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, help_text="Which school is offering this course?",)
    teacher = models.ForeignKey(
        Performer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="This selection box includes performers who teach at at least one school.",
    )
    start_time = models.DateTimeField(verbose_name="First class start time")
    lesson_duration = models.FloatField(verbose_name="Lesson duration in hours", help_text="How long is each lesson? Write the answer in decimal, for example two and a half hours should be written as 2.5.",)
    number_of_lessons = models.IntegerField(verbose_name="Total number of lessons", help_text="The total mumber of lessons in this course.",)
    class_show = models.BooleanField(verbose_name="Includes a class show")
    course_link = models.URLField(
        max_length=256, blank=True, verbose_name="Course Booking URL", help_text="A web page where students can find out more about this course, and book.",
    )

    @staticmethod
    def model_admin():
        return CourseAdmin

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
