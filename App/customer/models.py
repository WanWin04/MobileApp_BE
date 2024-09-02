from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} (ID: {self.customer_id})"
