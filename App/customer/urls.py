from django.urls import path
from .views import add_customer

urlpatterns = [
    path('add-customer/', add_customer, name='add_customer'),
]
