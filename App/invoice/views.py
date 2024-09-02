from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import SalesInvoice
from .serializers import SalesInvoiceSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from customer.models import Customer

class CreateSalesInvoiceView(generics.CreateAPIView):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoiceSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            invoice_serializer = SalesInvoiceSerializer(data=request.data, many=True)
        else:
            invoice_serializer = SalesInvoiceSerializer(data=[request.data], many=True)
        
        if invoice_serializer.is_valid():
            invoice_serializer.save(user=self.request.user)
            return Response({"message": "Sales invoices created successfully"}, status=201)
        else:
            return Response(invoice_serializer.errors, status=400)


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
