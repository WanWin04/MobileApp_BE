from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls) ,
    
    path('account/', include(('account.urls', 'account'), namespace='account')),
    path('invoice/', include(('invoice.urls', 'invoice'), namespace='invoice')),
    path('receipt/', include(('receipt.urls', 'receipt'), namespace='receipt')),
    path('book/', include(('book.urls', 'book'), namespace='book')),
    path('book-import-order/', include(('book_import_order.urls', 'book_import_order'), namespace='book_import_order')),
    path('report/', include(('report.urls', 'report'), namespace='report')),
    path('customer/', include(('customer.urls', 'customer'), namespace='customer')),
]