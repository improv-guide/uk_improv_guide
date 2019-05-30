from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    facebook_link = models.CharField(max_length=100)
