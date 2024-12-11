from django.contrib import admin

# Register your models here.
from .models import * 



class ProductCategoryAdmin(admin.ModelAdmin):
    list_display='name',
    search_fields='name',

class SupplierAdmin(admin.ModelAdmin):
    list_display='store_name','store_location','store_capacity','store_type'
    search_fields='store_name','store_location','store_capacity','store_type'
class ProductAdmin(admin.ModelAdmin):
    list_display = 'name','batch',
    search_fields='name','batch__batch_id',
class ProductBatchAdmin(admin.ModelAdmin):
    list_display='batch_id','expiry_date','is_expired','quantity','supplier'
    search_fields='batch_id','expiry_date','is_expired','quantity','supplier__name'
    list_filter='is_expired',

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductBatch,ProductBatchAdmin)
admin.site.register(Supplier,SupplierAdmin)