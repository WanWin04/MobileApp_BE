from django.urls import path
from .views import CreateImportBookOrderView, check_book_id

urlpatterns = [
    path('create-import-book-order/', CreateImportBookOrderView.as_view(), name='create_import_book_order'),
    path('check-book-id/', check_book_id, name='check_book_id'),
]