from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('account/', include(('account.urls', 'account'), namespace='account')),
    path('invoice/', include(('invoice.urls', 'invoice'), namespace='invoice')),
    path('receipt/', include(('receipt.urls', 'receipt'), namespace='receipt')),
]
