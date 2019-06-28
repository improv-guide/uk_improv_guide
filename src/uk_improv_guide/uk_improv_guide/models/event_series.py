import reversion
from django.db import models


@reversion.register
class EventSeries(models.Model):
    name = models.CharField(max_length=100)
