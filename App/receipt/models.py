from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Receipt(models.Model):
    receipt_id = models.AutoField(_("Receipt ID"), primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    customer_id = models.CharField(_('Customer ID'), null=True, max_length=10)
    customer_name = models.CharField(_('Customer Name'), max_length=250)
    address = models.CharField(_('Address'), max_length=250)
    phone_number = models.CharField(_('Phone Number'), max_length=20)
    email = models.EmailField(_('Email'), max_length=250)
    payment_date = models.DateField(_('Payment Date'))
    paid_amount = models.DecimalField(_('Payment Amount'), max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Receipt {self.receipt_id} for {self.customer_name}"
