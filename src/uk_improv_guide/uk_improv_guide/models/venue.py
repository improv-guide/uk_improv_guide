from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    facebook_link = models.CharField(max_length=256)
    website_link = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    postcode = models.CharField(max_length=10)
