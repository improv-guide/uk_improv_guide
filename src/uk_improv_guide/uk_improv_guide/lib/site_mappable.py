import datetime
from dataclasses import dataclass
from typing import Type

from django.http import HttpRequest
from django.db import models
from django.utils import timezone


@dataclass
class SiteMapInfo:
    loc: str
    lastmod: str
    changefreq: str = "monthly"
    priority: float = 0.8


def sitemap_model_object(url_base:str)->Type:
    class LinkableMixin:
        created_timestamp = models.DateTimeField(editable=False)
        updated_timestamp = models.DateTimeField(editable=False)

        def sitemap_url_data(self, request:HttpRequest, changefreq="monthly", priority=0.5)->SiteMapInfo:
            return SiteMapInfo(
                loc = request.build_absolute_uri(f"/{url_base}/{self.id}"),
                lastmod= self.updated_timestamp.isoformat(sep=" "),
                changefreq=changefreq,
                priority=priority
            )

        def save(self, *args, **kwargs):
            ''' On save, update timestamps '''
            print("XXXXXXXXXX UPDATING TIMESTAMOPS ")
            if not self.id:
                self.created = timezone.now()
            self.modified = timezone.now()
            return super(LinkableMixin, self).save(*args, **kwargs)

    return LinkableMixin
