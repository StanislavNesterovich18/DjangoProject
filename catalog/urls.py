from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
    path("contacts/", views.ContactsTemplateView.as_view(), name="contacts"),
    path("products/<int:pk>", views.ProductDetailView.as_view(), name="product_detail"),
]
