from django.urls import path
from orders.views import place_order, successful_donation, ship_products, mark_shipped_product

urlpatterns = [
    path('', place_order, name='place order'),
    path('successful-donation/<int:pk>', successful_donation, name='successful donation'),
    path('ship-products/', ship_products, name='ship products'),
    path('ship-products/<int:pk>', mark_shipped_product, name='mark shipped')
]