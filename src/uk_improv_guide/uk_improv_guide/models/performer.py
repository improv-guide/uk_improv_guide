from django.db import models


class Performer(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    facebook_link = models.CharField(max_length=100)
    contact_email_address = models.CharField(max_length=100)
