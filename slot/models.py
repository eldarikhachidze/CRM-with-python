from django.db import models
from django.utils import timezone

# Create your models here.


class SlotMachine(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    money_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_created = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(null=True, blank=True)
    date_deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Hall(models.Model):
    name = models.CharField(max_length=255)
    slot_machines = models.ManyToManyField(SlotMachine)
    date_created = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(null=True, blank=True)
    date_deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class GameDay(models.Model):
    date = models.DateField(default=timezone.now)
    slot_machines = models.ManyToManyField(SlotMachine, through='SlotMachineRecord')
    total_money = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    date_created = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(null=True, blank=True)
    date_deleted = models.DateTimeField(null=True, blank=True)

    def close_day(self):
        total = sum(record.money_at_end for record in self.slotmachinerecord_set.all())
        self.total_money = total
        self.save()

    def __str__(self):
        return f"Game Day: {self.date}"

class SlotMachineRecord(models.Model):
    slot_machine = models.ForeignKey(SlotMachine, on_delete=models.CASCADE)
    game_day = models.ForeignKey(GameDay, on_delete=models.CASCADE)
    money_at_end = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_created = models.DateTimeField(default=timezone.now)
    date_edited = models.DateTimeField(null=True, blank=True)
    date_deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.slot_machine} on {self.game_day}"