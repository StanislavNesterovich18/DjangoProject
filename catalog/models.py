from django.db import models

from users.models import User


class Category(models.Model):
    """Создание модели Category"""

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """Создание модели Product"""

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.FloatField(default=0, verbose_name="Цена за покупку")
    image = models.ImageField(upload_to="product/image/", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="list_products", verbose_name="Категория"
    )
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name="Владелец")
    is_publish = models.BooleanField(default=False, verbose_name="Публикация")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [("can_unpublish_product","Права на отмену публикации")]
