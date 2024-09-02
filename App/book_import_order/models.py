from django.db import models
from book.models import Book  # Giả sử model Book đã có trong app book

class ImportBookOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    date = models.DateField()

    def __str__(self):
        return str(self.order_id)

class OrderDetail(models.Model):
    order = models.ForeignKey(ImportBookOrder, on_delete=models.CASCADE, related_name='details')
    book_id = models.CharField(max_length=10, null=True, blank=True)  
    book_name = models.CharField(max_length=250, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    amount = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.order.order_id} - {self.book_name}"
