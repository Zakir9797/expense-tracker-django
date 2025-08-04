from django.db import models

class Entry(models.Model):
    ENTRY_TYPES = [
        ('expense', 'Expense'),
        ('income', 'Income'),
    ]
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    type = models.CharField(max_length=7, choices=ENTRY_TYPES)
    category = models.CharField(max_length=100)
    unit_price = models.FloatField()
    quantity = models.IntegerField(default=1)
    total_amount = models.FloatField()
    description = models.CharField(max_length=200, blank=True)
    currency = models.CharField(max_length=5, default="₸")

    def __str__(self):
        return f"{self.date} {self.time} | {self.type} | {self.category} | {self.total_amount}{self.currency}"