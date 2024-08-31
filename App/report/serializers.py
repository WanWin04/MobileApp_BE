from rest_framework import serializers
from .models import InventoryReport, DebtReport

class InventoryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryReport
        fields = ['user', 'month', 'book_name', 'begin', 'arise', 'end']
        extra_kwargs = {
            'user': {'read_only': True},
        }
        

class DebtReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtReport
        fields = ['user' ,'month', 'customer_name', 'begin', 'arise', 'end']
        extra_kwargs = {
            'user': {'read_only': True},
        }
