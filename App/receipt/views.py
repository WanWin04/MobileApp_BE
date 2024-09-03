from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Receipt
from .serializers import ReceiptSerializer

from rest_framework import serializers


class CreateReceiptView(generics.CreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

