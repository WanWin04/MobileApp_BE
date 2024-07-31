from rest_framework import serializers
from .models import Receipt


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = [
            'id',
            'user',
            'user_id'
            'customer_name',
            'address',
            'email',
            'payment_date',
            'paid_amount'
        ]
        extra_kwargs = {
            'user_id': {'read_only': True},
            'user': {'read_only': True},
            'id': {'read_only': True},
        }
