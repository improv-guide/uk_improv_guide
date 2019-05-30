from django.contrib import admin

from uk_improv_guide.models import ALL_MODELS

for m in ALL_MODELS:
    admin.site.register(m)