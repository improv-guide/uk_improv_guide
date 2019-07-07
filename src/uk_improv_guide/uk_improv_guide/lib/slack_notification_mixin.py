import logging

import requests

log = logging.getLogger(__name__)


class SlackNotificationMixin:
    def save(self, *args, **kwargs):
        result = super(SlackNotificationMixin, self).save(*args, **kwargs)
        log.warning("**** MAGIC IS ABOUT TO HAPPEN!!!!")
        return result
