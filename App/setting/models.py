from django.db import models

class RegulationSetting(models.Model):
    min_import_amount = models.PositiveIntegerField(default=50, help_text="Số lượng nhập tối thiểu.")
    max_import_stock = models.PositiveIntegerField(default=100, help_text="Chỉ nhập kho khi số lượng dưới mức này.")
    max_debt = models.DecimalField(max_digits=10, decimal_places=2, default=500000.00, help_text="Mức nợ tối đa.")
    min_stock = models.PositiveIntegerField(default=300, help_text="Số lượng tồn kho tối thiểu.")
    payment_bill_limit = models.BooleanField(default=False, help_text="Hóa đơn thanh toán của khách hàng không được vượt quá mức nợ.")

    def __str__(self):
        return "Regulation Settings"