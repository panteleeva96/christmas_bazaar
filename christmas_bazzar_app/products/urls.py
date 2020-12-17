from django.urls import path

from products.views import get_products, create_product, product_details, edit_product, delete_product

urlpatterns = [
    path('', get_products, name='products list'),
    path('create/', create_product, name='add product'),
    path('product/<int:pk>', product_details, name='detailed product'),
    path('edit/<int:pk>', edit_product, name='edit product'),
    path('delete/<int:pk>', delete_product, name='delete product'),
]