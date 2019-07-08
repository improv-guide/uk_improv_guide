import logging

import requests

from src.uk_improv_guide.uk_improv_guide.settings import SLACK_WEB_HOOK

log = logging.getLogger(__name__)


class SlackNotificationMixin:
    def save(self, *args, **kwargs):
        result = super(SlackNotificationMixin, self).save(*args, **kwargs)


        requests.post(url=SLACK_WEB_HOOK, data={"An object was updated!"})

        return result
