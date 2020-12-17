from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from products.forms import ProductForm
from products.models import Product


def get_products(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'products/products_list.html', context)


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
            form.save()
            return redirect('products list')

        context = {
            'form': form
        }
        return render(request, 'products/add_product.html', context)


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
        'can_edit': product.sold_by.id == request.user.id,
        'can_delete': product.sold_by.id == request.user.id,
        'can_buy': product.sold_by.id != request.user.id
    }
    return render(request, 'products/product_details.html', context)


def edit_product(request):
    pass


def delete_product(request):
    pass
