from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page
from django.conf import settings
from products.models import Product
from products.forms import ProductModelForm

# Create your views here.


# @cache_page(settings.CACHE_TTL)
def list_products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/list.html", context=context)


def create_product(request):
    form = ProductModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("products:list")

    context = {"form": form}
    return render(request, "products/create.html", context=context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect("products:list")


def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductModelForm(data=request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect("products:list")

    context = {"form": form}

    return render(request, "products/update.html", context=context)
