from django.urls import path
from .views import CreateSalesInvoiceView, check_customer_id

urlpatterns = [
    path('create-invoice/', CreateSalesInvoiceView.as_view(), name='create-sales-invoice'),
    path('check-customer-id/', check_customer_id, name='check_customer_id'),
]
