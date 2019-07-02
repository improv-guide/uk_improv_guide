import uuid

import reversion
from django.db import models


@reversion.register
class EventSeries(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="event_series/", blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
