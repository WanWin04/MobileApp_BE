from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

class SalesInvoice(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    customer_id = models.CharField(_('Customer ID'), max_length=10, null=True, blank=True)
    date = models.DateField(_('Date'))
    book_name = models.CharField(_('Book Name'), max_length=250)
    category = models.CharField(_('Category'), max_length=250)
    quantity = models.PositiveIntegerField(_("Quantity"))
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2, null=True, blank=True, default=0.00)
    
    def __str__(self):
        return f"Invoice {self.id} for {self.customer_id}"
