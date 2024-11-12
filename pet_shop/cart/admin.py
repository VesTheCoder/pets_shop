from django.contrib import admin
from .models import Order


# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'total', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('user', 'status', 'created_at', 'updated_at')
        }),
        ('Contact Information', {
            'fields': ('first_name', 'last_name', 'company', 'phone', 'email')
        }),
        ('Address Information', {
            'fields': ('country', 'address_line_1', 'address_line_2', 'city', 'zip_code')
        }),
        ('Order Details', {
            'fields': ('items', 'subtotal', 'shipping_cost', 'total', 'order_notes')
        }),
    )

