from django.contrib import admin
from .models import ImportBookOrder, OrderDetail

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 1

class ImportBookOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'date')
    inlines = [OrderDetailInline]  # Sử dụng inlines để hiển thị OrderDetail liên quan
    search_fields = ('order_id', 'date')

admin.site.register(ImportBookOrder, ImportBookOrderAdmin)
admin.site.register(OrderDetail)
