from rest_framework import generics
from .models import RegulationSetting
from .serializers import RegulationSettingSerializer
from rest_framework.permissions import IsAuthenticated

class RegulationSettingView(generics.RetrieveUpdateAPIView):
    queryset = RegulationSetting.objects.all()
    serializer_class = RegulationSettingSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return RegulationSetting.objects.first()