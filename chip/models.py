from django.db import models
from django.utils import timezone

class Chip(models.Model):
    denomination = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)  # Set default to current time
    date_edited = models.DateTimeField(null=True, blank=True)
    date_deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.denomination} (Created: {self.date_created})"
