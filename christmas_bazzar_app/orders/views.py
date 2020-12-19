import datetime

from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.
from campaigns.models import Campaign
from orders.forms import OrderForm
from orders.models import Order
from products.models import Product, Cart


def set_sold_products_unavailable(current_user, current_order):
    for product in Product.objects.filter(cart__user=current_user):
        product.order = current_order
        product.is_available = False
        product.save()


def update_raised_money(amount):
    campaign = Campaign.objects.first()
    campaign.raised_money += amount
    campaign.save()


def empty_user_cart(current_user):
    for cart_rec in Cart.objects.filter(user=current_user):
        cart_rec.delete()


@transaction.atomic
def place_order(request):
    if request.method == 'GET':
        total_amount = round(sum([product.price for product in Product.objects.filter(cart__user=request.user)]), 2)
        order = Order()
        order.amount = total_amount
        context = {
            'form': OrderForm(instance=order),
        }
        return render(request, 'orders/order_details.html', context)
    else:
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.buyer = request.user
            order.order_date = datetime.datetime.now()
            order.save()

            set_sold_products_unavailable(request.user, order)

            update_raised_money(order.amount)

            empty_user_cart(request.user)

            return redirect('successful donation', order.id)

        context = {
            'form': form,
        }
        return render(request, 'orders/order_details.html', context)


def successful_donation(request, pk):
    order = Order.objects.get(pk=pk)
    context = {
        'order': order
    }
    return render(request, 'orders/successful-donation.html', context)


def ship_products(request):
    context = {
        'products': Product.objects.filter(is_shipped=False, is_available=False, sold_by=request.user)
    }
    return render(request, 'orders/shipping_products.html', context)


def mark_shipped_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.is_shipped = True
    product.save()
    return redirect('ship products')