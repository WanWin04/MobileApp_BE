from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class SalesInvoice(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    customer_name = models.CharField(_('Customer Name'), max_length=250)
    date = models.DateField(_('Date'))
    book_name = models.CharField(_('Book Name'), max_length=250)
    category = models.CharField(_('Category'), max_length=250)
    quantity = models.PositiveIntegerField(_("Quantity"))
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Invoice {self.id} for {self.customer_name}"
