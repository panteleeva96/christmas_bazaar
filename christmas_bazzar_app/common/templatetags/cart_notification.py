from django import template

from products.models import Cart

register = template.Library()


@register.inclusion_tag('tags/cart_symbol.html')
def update_notification_in_cart(user):
    products_in_cart = len(Cart.objects.filter(user=user))
    return {
        'products_in_cart': products_in_cart
    }


