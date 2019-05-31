from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    facebook_link = models.CharField(max_length=256, blank=True)
    website_link = models.CharField(max_length=256, blank=True)
    google_maps_link = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, verbose_name="Street Address")
    city = models.CharField(max_length=256, default="London")
    postcode = models.CharField(max_length=10, verbose_name="Post Code")

    def __str__(self)->str:
        return f"{self.name}, {self.address}"
