from typing import MutableMapping, Type

from django.contrib.sitemaps import Sitemap
from django.db import models

GLOBAL_SITEMAPS: MutableMapping[str, Type[Sitemap]] = {}


class BaseSiteMap(Sitemap):
    def items(self):
        return self.model.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.pub_date


def make_sitemap_for_model(
    model: Type[models.Model], changefreq: str = "never", priority: float = 0.5
) -> Type[Sitemap]:
    sitemap_name = f"{model.__name__}"
    class_args = {"model": model, "changefreq": changefreq, "priority": priority}
    sitemap_type: Type[Sitemap] = type(sitemap_name, (BaseSiteMap,), class_args)
    return sitemap_type


def sitemap_for_model(model: models.Model, **kwargs) -> Type[Sitemap]:
    return GLOBAL_SITEMAPS.setdefault(
        model.__name__, make_sitemap_for_model(model, **kwargs)
    )


def register_model_for_site_map(m: Type[models.Model]) -> models.Model:
    sitemap_for_model(m)
    return m
