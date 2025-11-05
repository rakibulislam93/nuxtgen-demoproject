from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    payment_id = models.CharField(max_length=100)
    trx_id = models.CharField(max_length=100, blank=True, null=True)
    invoice = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.invoice} - {self.status}"