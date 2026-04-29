from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Настройки интерфейса администрирования для модели Product"""
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройки интерфейса администрирования для модели Category"""
    list_display = (
        "id",
        "name",
    )
    list_filter = ("name",)
