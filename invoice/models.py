from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    invoice_no = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Invoice {self.invoice_no}"