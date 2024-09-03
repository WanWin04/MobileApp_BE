from rest_framework import serializers
from .models import SalesInvoice

class SalesInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = [
            'id',
            'user',
            'customer_id',
            'customer_name',
            'date',
            'book_id',
            'book_name',
            'quantity',
            'price'
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'id': {'required': True},
        }
