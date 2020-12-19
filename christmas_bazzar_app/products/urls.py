from django.urls import path

from products.views import create_product, edit_product, delete_product, add_to_cart, \
    cart_list, remove_from_cart, ProductListView, ProductDetailsView

urlpatterns = [
    path('', ProductListView.as_view(), name='products list'),
    path('create/', create_product, name='add product'),
    # path('product/<int:pk>', product_details, name='detailed product'),
    path('product/<int:pk>', ProductDetailsView.as_view(), name='detailed product'),
    path('edit/<int:pk>', edit_product, name='edit product'),
    path('delete/<int:pk>', delete_product, name='delete product'),
    path('add_to_cart/<int:pk>', add_to_cart, name='add to cart'),
    path('my-cart/', cart_list, name='products in my cart'),
    path('remove-from-cart/<int:pk>', remove_from_cart, name='remove from cart'),
]