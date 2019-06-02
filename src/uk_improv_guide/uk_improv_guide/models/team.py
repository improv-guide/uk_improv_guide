from django.db import models

from uk_improv_guide.models.performer import Performer


class Team(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    facebook_link = models.CharField(max_length=100, blank=True, default="")
    contact_email_address = models.CharField(max_length=100, blank=True, default="")
    players = models.ManyToManyField(
        Performer,
        verbose_name="Team members",
        blank=True,
        related_name="plays_for"
    )

    def ___str__(self):
        return self.name

