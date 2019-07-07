from dataclasses import dataclass
from typing import Optional

from django.db import models
from django.http import HttpRequest


@dataclass
class SiteMapInfo:
    loc: str
    lastmod: Optional[str]
    changefreq: str = "monthly"
    priority: float = 0.8


class SiteMapThing:
    def sitemap_url_data(
        self, request: HttpRequest, changefreq="monthly", priority=0.5
    ) -> SiteMapInfo:
        return SiteMapInfo(
            loc=request.build_absolute_uri(f"/{self.url_base}/{self.id}"),
            lastmod=None,
            changefreq=changefreq,
            priority=priority,
        )
