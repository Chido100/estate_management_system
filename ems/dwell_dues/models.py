from django.db import models
from users.models import User



UTILITY_BILL = (
    ('', 'Select utility type'),
    ('electricity', 'Electricity'),
    ('water', 'Water'),
    ('bin collection', 'Bin Collection'),
)


class Dues(models.Model):
    utility_bill = models.CharField(max_length=20, choices=UTILITY_BILL)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')
    creditor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='due_creditor')
    payment_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-payment_date']
        verbose_name_plural = 'Dwell Dues'

    def __str__(self):
        return f'{self.creditor.full_name}'


