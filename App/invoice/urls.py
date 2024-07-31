from django.urls import path
from .views import CreateSalesInvoiceView

urlpatterns = [
    path('create-invoice/', CreateSalesInvoiceView.as_view(), name='create-sales-invoice'),
]
