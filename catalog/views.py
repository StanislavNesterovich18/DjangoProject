from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, UpdateView, DeleteView, CreateView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = "products"


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = "product"
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = "product"
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    context_object_name = "product"
    success_url = reverse_lazy('catalog:home')
