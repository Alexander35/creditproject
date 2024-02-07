from django.contrib import admin

from .models import CreditOrder, Contract, Vendor, Product

@admin.register(CreditOrder)
class CreditOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'credit_order', 'created_at')

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'credit_order', 'vendor', 'created_at')
