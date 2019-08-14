import logging

import requests
from uk_improv_guide import settings

log = logging.getLogger(__name__)


class SlackNotificationMixin:
    # def save(self, *args, **kwargs):
    #     result = super(SlackNotificationMixin, self).save(*args, **kwargs)
    #     log.info(f"About to ping {settings.SLACK_WEB_HOOK}")
    #     message = pprint.pformat(kwargs)
    #     requests.post(
    #         url=settings.SLACK_WEB_HOOK,
    #         data={f"An object was updated: {message}".encode("UTF-8")},
    #     )
    #     return result
    pass
