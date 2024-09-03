from rest_framework import serializers
from .models import Receipt


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = [
            'receipt_id',
            'user',
            'customer_id',
            'customer_name',
            'address',
            'phone_number',
            'email',
            'payment_date',
            'paid_amount'
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'receipt_id': {'required': True},
        }
