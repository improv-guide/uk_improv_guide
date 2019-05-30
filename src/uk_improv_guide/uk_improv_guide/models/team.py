from django.db import models

from uk_improv_guide.models.performer import Performer


class Team(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    facebook_link = models.CharField(max_length=100, blank=True, default="")
    contact_email_address = models.CharField(max_length=100, blank=True, default="")
    # contact_person = venue = models.ForeignKey(
    #     Performer,
    #     on_delete=models.SET_NULL
    # )
    players = models.ManyToManyField(Performer, verbose_name="Team members", blank=True)

