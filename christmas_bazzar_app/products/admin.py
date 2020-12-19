from django.contrib import admin

# Register your models here.
from products.models import Product, Cart


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'order', 'is_shipped')


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)