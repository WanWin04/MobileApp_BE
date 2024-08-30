from django.db import models
from book.models import Book  # Giả sử model Book đã có trong app book

class ImportBookOrder(models.Model):
    order_id = models.CharField(max_length=10, primary_key=True)
    user_id = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.order_id

class OrderDetail(models.Model):
    order = models.ForeignKey(ImportBookOrder, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.order.order_id} - {self.book.book_name}"
