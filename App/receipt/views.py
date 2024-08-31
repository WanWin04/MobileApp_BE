from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Receipt
from .serializers import ReceiptSerializer


class CreateReceiptView(generics.CreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        receipt_id = self.request.data.get('receipt_id')
        
        if not receipt_id:
            raise serializers.ValidationError({'receipt_id': 'This field is required.'})

        serializer.save(user=self.request.user, receipt_id=receipt_id)
