from django.contrib import admin
from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'family_name', 'amount', 'order_date')


admin.site.register(Order, OrderAdmin)