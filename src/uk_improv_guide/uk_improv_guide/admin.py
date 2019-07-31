import logging
from typing import Type

from django.contrib import admin
from reversion.admin import VersionAdmin
from uk_improv_guide.models import ALL_MODELS

log = logging.getLogger(__name__)


def get_admin_class_for_model(m) -> Type:
    try:
        ac = m.model_admin
    except AttributeError:
        admin_name = f"{m.__name__}Admin"
        log.debug(f"No custom admin found for {m}")
        ac = type(admin_name, (VersionAdmin,), {"save_as": True})
        globals()[admin_name] = ac
    return ac


for m in ALL_MODELS:
    admin.register(m)(get_admin_class_for_model(m))
