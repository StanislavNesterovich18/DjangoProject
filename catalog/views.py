from django.shortcuts import render

from catalog.models import Product


def home(request):
    list_products = Product.objects.all()
    return render(request, "catalog/home.html", {"products": list_products})


def contacts(request):
    return render(request, "catalog/contacts.html")


def product_info(request, pk_product):
    product = Product.objects.filter(pk=pk_product).first()
    return render(request, "catalog/product_detail.html", {"product": product})
