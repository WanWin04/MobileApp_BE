from rest_framework import serializers
from .models import ImportBookOrder, OrderDetail
from setting.models import RegulationSetting
from book.models import Book

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['book_id', 'book_name', 'author', 'amount']  

class ImportBookOrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True)  

    class Meta:
        model = ImportBookOrder
        fields = ['order_id', 'date', 'details']

    def validate(self, data):
        regulation = RegulationSetting.objects.first()
        if not regulation:
            raise serializers.ValidationError("The system regulations not found.")

        for detail in data['details']:
            try:
                book = Book.objects.get(book_id=detail['book_id'])
            except Book.DoesNotExist:
                raise serializers.ValidationError(f"(ID: {data['book_id']}) Book does not exist.")
            
            if detail['amount'] < regulation.min_import_amount:
                raise serializers.ValidationError (f"(ID: {detail['book_id']}) The minimum import quantity is {regulation.min_import_amount}. Currently, there are only {detail['amount']}.")
            
            current_stock = book.amount
            if current_stock >= regulation.max_import_stock:
                raise serializers.ValidationError(f"(ID: {book.book_id}) The quantity of books in stock has exceeded the allowed maximum import limit of {regulation.max_import_stock}.")

        return data
    
    def create(self, validated_data):
        details_data = validated_data.pop('details')
        order = ImportBookOrder.objects.create(**validated_data)
        for detail_data in details_data:
            OrderDetail.objects.create(order=order, **detail_data)
            
            try:
                book = Book.objects.get(book_id=detail_data['book_id'])
                book.amount += detail_data['amount']
                book.save()
            except Book.DoesNotExist:
                pass

        return order
            