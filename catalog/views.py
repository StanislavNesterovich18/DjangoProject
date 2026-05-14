from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from catalog.forms import ProductForm, ProductFormModeration
from catalog.models import Category, Product
from catalog.services import products_category_view


class ProductListView(ListView):
    """Работа со списком продуктов"""

    model = Product
    context_object_name = "products"

    def get_queryset(self):
        """Получение списка опубликованных продуктов"""
        queryset = cache.get("products")
        if queryset is None:
            queryset = Product.objects.filter(is_publish=True)
            cache.set("products", queryset, 60 * 5)
        return queryset


class ContactsTemplateView(TemplateView):
    """Контроллер отоброжение контактов"""

    template_name = "catalog/contacts.html"


@method_decorator(cache_page(60 * 15), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    """Работа с деталями продукта"""

    model = Product
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Обновление продукта"""

    model = Product
    form_class = ProductForm
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")
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
    success_url = reverse_lazy("catalog:home")
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
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super().form_valid(form)


class ListProductsCategoryView(DetailView):
    model = Category
    context_object_name = "products_category"
    template_name = "catalog/products_list_category.html"

    def get_context_data(self, **kwargs):
        context = super(ListProductsCategoryView, self).get_context_data(**kwargs)
        obj_category = self.kwargs.get("pk", None)
        category = Category.objects.filter(pk=obj_category).first()
        context["products"] = products_category_view(category)
        return context

    def get_queryset(self):
        """Получение списка опубликованных продуктов"""
        queryset = cache.get("products_category")
        if queryset is None:
            queryset = super().get_queryset()
            cache.set("products_category", queryset, 60 * 5)
        return queryset
