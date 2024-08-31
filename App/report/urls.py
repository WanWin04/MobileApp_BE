from django.urls import path
from .views import InventoryReportView, DebtReportView

urlpatterns = [
    path('inventory/', InventoryReportView.as_view(), name='inventory_report'),
    path('debt/', DebtReportView.as_view(), name='debt_report'),
]
