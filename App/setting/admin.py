from django.contrib import admin
from .models import RegulationSetting

class RegulationSettingAdmin(admin.ModelAdmin):
    list_display = ('min_import_amount', 'max_import_stock', 'max_debt', 'min_stock', 'payment_bill_limit')
    list_display_links = ('min_import_amount',)
    list_editable = ('max_import_stock', 'max_debt', 'min_stock', 'payment_bill_limit')

    def get_queryset(self, request):
        RegulationSetting.objects.get_or_create(
            defaults={
                'min_import_amount': 150,
                'max_import_stock': 300,
                'max_debt': 300,
                'min_stock': 300,
                'payment_bill_limit': False
            }
        )
        return super().get_queryset(request)

admin.site.register(RegulationSetting, RegulationSettingAdmin)