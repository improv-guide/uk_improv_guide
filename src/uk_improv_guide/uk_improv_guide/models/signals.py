import logging

from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

log = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance: User, created, **kwargs):
    if created:
        instance.is_staff = True
        group: Group = Group.objects.get(name="site_administrators")
        log.info(f"Adding group {group} to user: {instance}")
        instance.groups.add(group)
        instance.save()
