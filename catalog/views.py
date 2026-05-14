from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, UpdateView, DeleteView, CreateView

from catalog.forms import ProductForm, ProductFormModeration
from catalog.models import Product


class ProductListView(ListView):
    """Работа со списком продуктов"""
    model = Product
    context_object_name = "products"
    def get_queryset(self):
        """Получение списка опубликованных продуктов"""
        return Product.objects.filter(is_publish=True)


class ContactsTemplateView(TemplateView):
    """Контроллер отоброжение контактов"""
    template_name = "catalog/contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Работа с деталями продукта"""
    model = Product
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Обновление продукта"""
    model = Product
    form_class = ProductForm
    context_object_name = "product"
    success_url = reverse_lazy('catalog:home')
    permission_required = "catalog.can_unpublish_product"

    def get_form_class(self):
        user = self.request.user
        product = self.object

        if user.has_perm("catalog.can_unpublish_product"):
            return ProductFormModeration
        elif product.owner == user:
            return ProductForm

        return PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Удаление продукта"""
    model = Product
    context_object_name = "product"
    success_url = reverse_lazy('catalog:home')
    permission_required = "catalog.delete_product"

    def get_form_class(self):
        user = self.request.user
        product = self.object
        if product.owner == user or user.has_perm("catalog.delete_product"):
            return ProductFormModeration
        return PermissionDenied


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание продукта"""
    model = Product
    form_class = ProductForm
    context_object_name = "product"
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)
