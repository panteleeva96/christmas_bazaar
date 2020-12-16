from django.urls import path

from products.views import get_products, create_product, product_details

urlpatterns = [
    path('', get_products, name='products list'),
    path('create/', create_product, name='add product'),
    path('product/<int:pk>', product_details, name='detailed product'),

]