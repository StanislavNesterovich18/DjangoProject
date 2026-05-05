from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройки интерфейса администрирования для модели User"""

    list_display = ("id", "email")


