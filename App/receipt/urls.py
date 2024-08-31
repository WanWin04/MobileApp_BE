from django.urls import path
from .views import CreateReceiptView

urlpatterns = [
    path('create-receipt/', CreateReceiptView.as_view(), name='create-receipt'),
]
