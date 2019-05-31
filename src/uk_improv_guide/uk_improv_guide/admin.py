from django.contrib import admin
from reversion.admin import VersionAdmin

from uk_improv_guide.models import ALL_MODELS

for m in ALL_MODELS:
    @admin.register(m)
    class YourModelAdmin(VersionAdmin):
        pass

