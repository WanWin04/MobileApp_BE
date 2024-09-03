from django.apps import AppConfig
from django.db.utils import OperationalError

class SettingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "setting"

    def ready(self):
        from .models import RegulationSetting
        try:
            if not RegulationSetting.objects.exists():
                RegulationSetting.objects.create(
                    min_import_amount=150,
                    max_import_stock=300,
                    max_debt=300,
                    min_stock=300,
                    payment_bill_limit=False
                )
        except OperationalError:
            pass