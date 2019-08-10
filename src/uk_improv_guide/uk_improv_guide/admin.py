import logging
from typing import Type

from django.contrib import admin
from reversion.admin import VersionAdmin
from uk_improv_guide.models import get_all_models

log = logging.getLogger(__name__)


def get_standard_admin_class(m):
    admin_name = f"{m.__name__}Admin"
    log.debug(f"No custom admin found for {m}")
    ac = type(admin_name, (VersionAdmin,), {"save_as": True})
    globals()[admin_name] = ac
    return ac


def get_admin_class_for_model(m) -> Type:
    try:
        ac = m.model_admin()
        log.info(f"Using custom admin class for {m}.")
    except AttributeError:
        log.info(f"Using standard admin class for {m}.")
        ac = get_standard_admin_class(m)

    return ac


for m in get_all_models():
    # admin.site.register(m, MarkdownxModelAdmin)

    admin.register(m)(get_admin_class_for_model(m))
