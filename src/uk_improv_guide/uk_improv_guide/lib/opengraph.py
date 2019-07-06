from dataclasses import dataclass
from typing import Iterator

from django.db import models
from django.http import HttpRequest


@dataclass
class OpengraphItem:
    name: str
    content: str


def opengraph_person(
    title: str,
    first_name: str,
    family_name: str,
    image: models.ImageField,
    request: HttpRequest,
) -> Iterator[OpengraphItem]:
    image_url = request.build_absolute_uri(f"/{image.url}") if image else "xxx"
    yield from og_headers(
        title=title,
        url=request.build_absolute_uri(),
        image=image_url,
        type="profile",
        **{"profile:first_name": first_name, "profile:last_name": family_name},
    )


def opengraph_website(
    title: str, image: models.ImageField, request: HttpRequest, **kwargs
) -> Iterator[OpengraphItem]:
    image_url = request.build_absolute_uri(f"/{image.url}") if image else None
    yield from og_headers(
        title=title,
        url=request.build_absolute_uri(),
        image=image_url,
        type="website",
        **kwargs,
    )


def og_headers(**kwargs) -> Iterator[OpengraphItem]:
    for k, v in kwargs.items():
        if v:
            yield OpengraphItem(k, v)
