from django.db import models


class Blog(models.Model):
    """Создание модели страницы"""

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Cодержимое", blank=True, null=True)
    preview = models.ImageField(upload_to="blog/image/", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_publish = models.BooleanField(default=False, verbose_name="Признак Публикации")
    count_views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
