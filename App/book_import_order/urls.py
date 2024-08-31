from django.urls import path
from .views import create_import_book_order

urlpatterns = [
    path('create-import-order/', create_import_book_order, name='create_book_import_order'),
]
