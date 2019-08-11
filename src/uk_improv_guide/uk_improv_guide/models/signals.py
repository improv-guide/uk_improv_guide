import logging

from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

log = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_user_profile(
    sender, instance: User, created, default_group_name: str = "site_users", **kwargs
):
    instance.is_staff = True
    log.warning(f"Set permissions for {default_group_name}")

    try:
        group: Group = Group.objects.get(name=default_group_name)
    except Group.DoesNotExist:
        log.warning(f"Creating new group: {default_group_name}")
        group = Group(name=default_group_name)
        group.save()

    if group not in instance.groups.all():
        log.info(f"Adding group {group} to user: {instance}")
        instance.groups.add(group)
        instance.save()
