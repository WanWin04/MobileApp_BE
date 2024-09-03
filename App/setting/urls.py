from django.urls import path
from .views import RegulationSettingView

urlpatterns = [
    path('regulations/', RegulationSettingView.as_view(), name='regulations'),
]
