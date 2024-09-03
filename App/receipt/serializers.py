from rest_framework import serializers
from .models import Receipt
from customer.models import Customer
from setting.models import RegulationSetting

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
        
    def create(self, validated_data):
        receipt = Receipt.objects.create(**validated_data)
        
        regulation = RegulationSetting.objects.first()
        if not regulation:
            raise serializers.ValidationError("The system regulations not found.")
        
        try:
            customer = Customer.objects.get(customer_id=validated_data['customer_id'])
        except Customer.DoesNotExist:
            raise serializers.ValidationError(f"(ID: {validated_data['customer_id']}) Customer not exist.")

        if regulation.payment_bill_limit and customer.debt < validated_data['paid_amount']:
            raise serializers.ValidationError("Customer's payment bill don't exceed debt.")
        customer.debt -= validated_data['paid_amount']
        customer.save()

        return receipt

    