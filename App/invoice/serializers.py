from rest_framework import serializers
from .models import SalesInvoice
from customer.models import Customer
from setting.models import RegulationSetting
from book.models import Book

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
        
    def validate(self, data):
        regulation = RegulationSetting.objects.first()
        if not regulation:
            raise serializers.ValidationError("The system regulations not found.")
        
        try:
            customer = Customer.objects.get(customer_id=data['customer_id'])
        except Customer.DoesNotExist:
            raise serializers.ValidationError(f"(ID: {data['customer_id']}) Customer not exist.")

        total_price = data['quantity'] * data['price']

        if customer.debt + total_price > regulation.max_debt:
            raise serializers.ValidationError(
                f"ID {data['customer_id']} Customer does not meet the purchasing criteria. "
                f"Current debt + New total amount of {total_price} exceed the allowed debt limit of {regulation.max_debt}."
            )

        return data
    
    def create(self, validated_data):
        invoice = SalesInvoice.objects.create(**validated_data)
        
        try:
            customer = Customer.objects.get(customer_id=validated_data['customer_id'])
        except Customer.DoesNotExist:
            raise serializers.ValidationError(f"(ID: {validated_data['customer_id']}) Customer does not exist.")

        try:
            book = Book.objects.get(book_id=validated_data['book_id'])
        except Book.DoesNotExist:
            raise serializers.ValidationError(f"(ID: {validated_data['book_id']}) Book does not exist.")
        
        total_price = validated_data['quantity'] * validated_data['price']
        customer.debt += total_price
        book.amount -= validated_data['quantity']
        
        customer.save()
        book.save()

        return invoice