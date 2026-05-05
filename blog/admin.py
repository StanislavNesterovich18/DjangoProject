from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Настройки интерфейса администрирования для модели Blog"""

    list_display = (
        "id",
        "title",
        "content",
        "preview",
        "created_at",
        "is_publish",
        "count_views",
    )
    list_filter = ("is_publish",)
    search_fields = (
        "title",
        "content",
    )
