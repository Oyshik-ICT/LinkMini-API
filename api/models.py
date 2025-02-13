from django.db import models
from django.utils import timezone


class UrlMapping(models.Model):
    """
    Model for mapping short URLs to long URLs.
    """

    short_url = models.CharField(max_length=20, db_index=True)
    long_url = models.CharField(max_length=3000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.long_url
