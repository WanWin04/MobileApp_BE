from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import InventoryReport, DebtReport
from .serializers import InventoryReportSerializer, DebtReporterSerializer

class InventoryReportView(generics.CreateAPIView):
    queryset = InventoryReport.objects.all()
    serializer_class = InventoryReportSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        inventory_data = request.data
        inventory_serializer = InventoryReportSerializer(data=inventory_data, many=True)
        if inventory_serializer.is_valid():
            inventory_serializer.save(user=self.request.user)
            return Response({"message": "Inventory report created successfully"}, status=201)
        else:
            return Response(inventory_serializer.errors, status=400)
        
class DebtReportView(generics.CreateAPIView):
    queryset = DebtReport.objects.all()
    serializer_class = DebtReporterSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        debt_data = request.data
        debt_serializer = DebtReporterSerializer(data=debt_data, many=True)
        if debt_serializer.is_valid():
            debt_serializer.save(user=self.request.user)
            return Response({"message": "Debt report created successfully"}, status=201)
        else:
            return Response(debt_serializer.errors, status=400)
