from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import ListView, DetailView

from products.forms import ProductForm
from products.models import Product, Cart


class ProductListView(ListView):
    template_name = 'products/products_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = self.model.objects.exclude(sold_by=self.request.user).filter(is_available=True)
            return qs
        return self.model.objects.all()




class ProductDetailsView(DetailView):
    template_name = 'products/product_details.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_product = context['product']
        context['can_delete'] = current_product.sold_by == self.request.user
        context['can_edit'] = current_product.sold_by == self.request.user
        context['can_buy'] = current_product.sold_by != self.request.user

        return context


@login_required
def create_product(request):
    if request.method == "GET":
        context = {
            'form': ProductForm(),
        }
        return render(request, 'products/add_product.html', context)
    else:
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.sold_by = request.user
            product.save()
            return redirect('user profile')

        context = {
            'form': form
        }
        return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "GET":
        context = {
            'product': product,
            'form': ProductForm(instance=product),
        }
        return render(request, 'products/edit_product.html', context)
    else:
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product.save()
            return redirect('user profile')

        context = {
            'form': form
        }
        return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'product': product,
        }
        return render(request, 'products/delete_product.html', context)
    else:
        product.delete()
        return redirect('user profile')


@login_required
def add_to_cart(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        cart = Cart(user=request.user, product=product)
        cart.save()
        return redirect('products list')
    except IntegrityError:
        return redirect('products list')


def cart_list(request):
    if request.method == 'GET':
        context = {
            'products': Product.objects.filter(cart__user=request.user),
            'total_amount': sum([product.price for product in Product.objects.filter(cart__user=request.user)])
        }
        return render(request, 'products/cart.html', context)


def remove_from_cart(request, pk):
    cart_product = Cart.objects.get(user=request.user, product=pk)
    cart_product.delete()
    return redirect('products in my cart')