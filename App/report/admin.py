from django.contrib import admin
from .models import InventoryReport, DebtReport

admin.site.register(InventoryReport)
admin.site.register(DebtReport)
