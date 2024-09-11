from django.db import models
from django.utils import timezone

# Create your models here.

class Table(models.Model):
    flot = models.JSONField(default=dict)  # Default to an empty JSON object
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Fleet: {self.flot}"