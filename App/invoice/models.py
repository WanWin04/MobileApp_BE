from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class SalesInvoice(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    customer_name = models.CharField(_('customer name'), max_length=250)
    date = models.DateField(_('date'))
    book_name = models.CharField(_('book name'), max_length=250)
    category = models.CharField(_('category'), max_length=250)
    quantity = models.PositiveIntegerField(_("quantity"))
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Invoice {self.id} for {self.customer_name}"
