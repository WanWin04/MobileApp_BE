from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
    
    
class InventoryReport(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    month = models.DateField(_('Month'))
    book_name = models.CharField(_('Book Name'), max_length=250)
    begin = models.IntegerField(_("Begin"))
    arise = models.IntegerField(_("Arise"))
    end = models.IntegerField(_("End"))

class DebtReport(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    month = models.DateField(_('Month'))
    customer_name = models.CharField(_('Customer Name'), max_length=250)
    begin = models.IntegerField(_("Begin"))
    arise = models.IntegerField(_("Arise"))
    end = models.IntegerField(_("End"))
