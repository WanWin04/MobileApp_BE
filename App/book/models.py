from django.db import models

class Book(models.Model):
    book_id = models.CharField(max_length=10, primary_key=True)
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='Uncategorized')
    price = models.IntegerField()
    amount = models.IntegerField(null=True, blank=True, default=0)
    cover = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.book_name
