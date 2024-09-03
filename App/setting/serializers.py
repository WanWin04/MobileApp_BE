from rest_framework import serializers
from .models import RegulationSetting
from customer.models import Customer 

class RegulationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegulationSetting
        fields = ['min_import_amount', 'max_import_stock', 'max_debt', 'min_stock', 'payment_bill_limit']
    def validate_max_debt(self, value):
        customers_with_high_debt = Customer.objects.filter(debt__gte=value)
        if customers_with_high_debt.exists():
            raise serializers.ValidationError(f"There are {customers_with_high_debt.count()} customers with debt greater than or equal to the new maximum debt limit.")

        return value

    def update(self, instance, validated_data):
        max_debt = validated_data.get('max_debt', instance.max_debt)
        self.validate_max_debt(max_debt)
        
        instance.min_import_amount = validated_data.get('min_import_amount', instance.min_import_amount)
        instance.max_import_stock = validated_data.get('max_import_stock', instance.max_import_stock)
        instance.max_debt = max_debt
        instance.min_stock = validated_data.get('min_stock', instance.min_stock)
        instance.payment_bill_limit = validated_data.get('payment_bill_limit', instance.payment_bill_limit)
        
        instance.save()
        return instance