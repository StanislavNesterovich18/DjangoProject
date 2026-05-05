from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, UpdateView, DeleteView, CreateView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    """Работа со списком продуктов"""
    model = Product
    context_object_name = "products"


class ContactsTemplateView(TemplateView):
    """Контроллер отоброжение контактов"""
    template_name = "catalog/contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Работа с деталями продукта"""
    model = Product
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Обновление продукта"""
    model = Product
    form_class = ProductForm
    context_object_name = "product"
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление продукта"""
    model = Product
    context_object_name = "product"
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание продукта"""
    model = Product
    form_class = ProductForm
    context_object_name = "product"
    success_url = reverse_lazy('catalog:home')
