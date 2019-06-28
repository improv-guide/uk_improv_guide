import uuid

import reversion
from django.db import models


@reversion.register
class EventSeries(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
