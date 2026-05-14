from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
    path("contacts/", views.ContactsTemplateView.as_view(), name="contacts"),
    path("products/<int:pk>", views.ProductDetailView.as_view(), name="product_detail_view"),
    path("products/create", views.ProductCreateView.as_view(), name="product_create_view"),
    path("products/<int:pk>/update/", views.ProductUpdateView.as_view(), name="product_update_view"),
    path("products/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete_view"),
    path("products/category/<int:pk>/", views.ListProductsCategoryView.as_view(), name="products_category"),
]
