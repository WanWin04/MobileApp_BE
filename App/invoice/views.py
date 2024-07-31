from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import SalesInvoice
from .serializers import SalesInvoiceSerializer


class CreateSalesInvoiceView(generics.CreateAPIView):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoiceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
