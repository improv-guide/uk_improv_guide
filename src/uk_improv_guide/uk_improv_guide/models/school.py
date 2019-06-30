import uuid

import reversion
from django.db import models


@reversion.register
class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="school/", blank=True)

    def __str__(self):
        return self.name
