import logging

from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

log = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance: User, created, default_group_name:str="site_users", **kwargs):
    if created:
        instance.is_staff = True

        try:
            group: Group = Group.objects.get(name=default_group_name)
        except Group.model.DoesNotExist:
            log.warning(f"Set permissions for {default_group_name}")
            group = Group(name=default_group_name)
            group.save()

        log.info(f"Adding group {group} to user: {instance}")
        instance.groups.add(group)
        instance.save()
