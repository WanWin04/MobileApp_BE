from rest_framework import serializers
from .models import ImportBookOrder, OrderDetail

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['book', 'amount']

class ImportBookOrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True)

    class Meta:
        model = ImportBookOrder
        fields = ['order_id', 'user_id', 'date', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        order = ImportBookOrder.objects.create(**validated_data)
        for detail_data in details_data:
            OrderDetail.objects.create(order=order, **detail_data)
        return order
