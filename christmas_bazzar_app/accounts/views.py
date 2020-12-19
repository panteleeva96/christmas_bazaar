from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import SignUpForm
from orders.models import Order
from products.models import Product


def user_profile(request):
    products_to_ship = Product.objects.filter(is_shipped=False, is_available=False, sold_by=request.user)
    context = {
        'products': Product.objects.filter(sold_by=request.user),
        'profile': request.user,
        'donated_money': sum([order.amount for order in Order.objects.filter(buyer=request.user)]),
        'products_to_ship': products_to_ship,
        'products_to_ship_count': len(products_to_ship),
        'owner': True,
    }
    return render(request, 'accounts/profile.html', context)


def signup_user(request):
    if request.method == 'GET':
        context = {
            'user_form': SignUpForm()
        }
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

        context = {
            'user_form': form
        }
        return render(request, 'accounts/signup.html', context)


def signout_user(request):
    logout(request)
    return redirect('index')