from django.db import models
from django.utils import timezone

# Create your models here.

class Slot_machine(models.Model):
    slot_name = models.CharField(max_length=100)
    slot_type = models.CharField(max_length=100)
    bv_count = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(null=True, blank=True)
    date_deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.slot_name