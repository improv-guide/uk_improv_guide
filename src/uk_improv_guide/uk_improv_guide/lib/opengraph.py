from dataclasses import dataclass
from typing import Iterator, Optional
from django.db import models

@dataclass
class OpengraphItem:
    name: str
    content: str


def url_from_image_field(imf:models.ImageField)->Optional[str]:
    return imf.url if imf else None

def opengraph_person(
    title: str, url: str, first_name: str, family_name: str, image: models.ImageField
) -> Iterator[OpengraphItem]:
    yield from og_headers(
        title=title,
        url=url,
        image=url_from_image_field(image),
        type="profile",
        **{"profile:first_name": first_name, "profile:last_name": family_name}
    )


def opengraph_website(
    title: str, url: str, image: models.ImageField, **kwargs
) -> Iterator[OpengraphItem]:
    yield from og_headers(title=title, url=url, image=url_from_image_field(image), type="website", **kwargs)


def og_headers(**kwargs) -> Iterator[OpengraphItem]:
    for k, v in kwargs.items():
        yield OpengraphItem(k, v)
