from django.db import models
from django.utils import timezone

# Create your models here.

class Table(models.Model):
    name = models.CharField(max_length=200, default="Default Table Name")
    open_flot = models.JSONField(default=dict)  # Default to an empty JSON object
    open_flot_total = models.FloatField(default=0.0)
    close_flot = models.JSONField(default=dict)  # Default to an empty JSON object
    close_flot_total = models.FloatField(default=0.0)
    result = models.FloatField(default=0.0)
    active = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(null=True, blank=True)
    date_deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Fleet: {self.flot}"