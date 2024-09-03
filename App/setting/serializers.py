from rest_framework import serializers
from .models import RegulationSetting

class RegulationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegulationSetting
        fields = ['min_import_amount', 'max_import_stock', 'max_debt', 'min_stock', 'payment_bill_limit']
