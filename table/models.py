from django.db import models

# Create your models here.

class Table(models.Model):
    denomination = models.DecimalField(max_digits=10, decimal_places=2)  # Store float-like values (e.g., 1.0, 5.0)
    quantity = models.PositiveIntegerField()  # The value in the dictionary (e.g., "20", "100")

    def __str__(self):
        return f"Denomination: {self.denomination}, Quantity: {self.quantity}"