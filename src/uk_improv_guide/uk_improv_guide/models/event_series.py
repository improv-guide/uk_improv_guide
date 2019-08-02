import uuid

import reversion
from django.db import models
from uk_improv_guide.lib.adminable import AdminableObject
from uk_improv_guide.lib.slack_notification_mixin import SlackNotificationMixin


@reversion.register
class EventSeries(SlackNotificationMixin, AdminableObject, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="event_series/", blank=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
