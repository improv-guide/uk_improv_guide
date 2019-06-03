from django.db import models
import reversion


@reversion.register
class EventSeries(models.Model):
    name = models.CharField(max_length=100, primary_key=True)