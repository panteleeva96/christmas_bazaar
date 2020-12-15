from django.shortcuts import render, redirect

# Create your views here.
from products.forms import ProductForm
from products.models import Product


def get_products(request):
    context = {
        'products': Product.objects.all(),

    }
    return render(request, 'products/products_list.html', context)


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


def edit_product(request):
    pass


def delete_product(request):
    pass
