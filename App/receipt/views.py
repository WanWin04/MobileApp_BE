from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Receipt
from .serializers import ReceiptSerializer


class CreateReceiptView(generics.CreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from customer.models import Customer

@api_view(['POST'])
def check_customer_id(request):
    customer_id = request.data.get('customer_id', None)
    
    if not customer_id:
        return Response({'error': 'Customer ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        customer = Customer.objects.get(customer_id=customer_id)
        return Response({'customer_name': customer.name}, status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)