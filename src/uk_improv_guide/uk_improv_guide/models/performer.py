from django.db import models
import reversion


@reversion.register
class Performer(models.Model):
    first_name = models.CharField(max_length=50, default="")
    family_name = models.CharField(max_length=50, default="")
    facebook_link = models.CharField(max_length=100, blank=True, default="")
    contact_email_address = models.CharField(max_length=100, blank=True, default="")

    def __str__(self)->str:
        return "%s %s" % (self.first_name, self.family_name)
